import os
import time
import tarfile
from datetime import datetime


def write_log(log_file, message):
    try:
        os.makedirs("logs", exist_ok=True)
        timestamp = datetime.now().strftime("[%d/%m/%Y %H:%M]")
        with open(log_file, "a") as file:
            file.write(f"{timestamp} {message}\n")
    except Exception as e:
        print("Logging error:", e)


def check_schedules():
    try:
        with open("backup_schedules.txt", "r") as file:
            lines = file.readlines()

        current_time = datetime.now()
        remaining_lines = []

        for line in lines:
            parts = line.strip().split(";")
            if len(parts) != 3:
                remaining_lines.append(line)
                continue

            name = parts[0]
            schedule_time_str = parts[1]
            folder = parts[2]

            try:
                schedule_time = datetime.strptime(schedule_time_str, "%H:%M").replace(
                    year=current_time.year,
                    month=current_time.month,
                    day=current_time.day,
                )

            except ValueError:
                remaining_lines.append(line)
                write_log(
                    "logs/backup_service.log",
                    f"Malformed schedule skipped: {line.strip()}",
                )
                continue

            if current_time >= schedule_time:

                os.makedirs("backups", exist_ok=True)

                # Step 12c — timestamped backups
                timestamp = datetime.now().strftime("%Y%m%d_%H%M")
                tar_path = f"backups/{folder}_{timestamp}.tar"

                try:
                    with tarfile.open(tar_path, "w") as tar:
                        tar.add(name, arcname=os.path.basename(name))

                    write_log("logs/backup_service.log", f"Backup created: {tar_path}")

                except Exception as e:
                    write_log(
                        "logs/backup_service.log", f"Error backing up {name}: {e}"
                    )

            else:
                remaining_lines.append(line)

        # Rewrite schedules
        with open("backup_schedules.txt", "w") as file:
            file.writelines(remaining_lines)

    except Exception:
        write_log("logs/backup_service.log", "Error reading schedules")


# SERVICE LOOP
write_log("logs/backup_service.log", "Backup service started")

while True:
    check_schedules()
    time.sleep(45)
