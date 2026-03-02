import os
import sys
import signal
import subprocess
from datetime import datetime


def init_environment():
    # Create logs folder
    os.makedirs("logs", exist_ok=True)
    # Create backups folder
    os.makedirs("backups", exist_ok=True)
    # Create schedules file if it doesn't exist
    if not os.path.exists("backup_schedules.txt"):
        with open("backup_schedules.txt", "w") as f:
            pass  # just create empty file


def write_log(log_file, message):
    try:
        # Step A: CREATE LOGS DIRECOTRY IF MISSING
        os.makedirs("logs", exist_ok=True)
        # Step B: GET TIMESTAMP
        timestamp = datetime.now().strftime("[%d/%m/%Y %H:%M]")
        # Step C: WRITE INTO THE LOG FILE
        with open(log_file, "a") as file:
            file.write(timestamp + " " + message + "\n")

    except Exception as e:
        print("Logging error:", e)


def create_schedule(schedule):

    try:

        parts = schedule.split(";")

        if len(parts) != 3:
            write_log(
                "logs/backup_manager.log", f"Error: malformed schedule: {schedule}"
            )
            return

        time_part = parts[1]

        # Your task: add ":" validation here
        if ":" not in time_part:
            write_log(
                "logs/backup_manager.log", f"Error: malformed schedule time: {schedule}"
            )
            return

        with open("backup_schedules.txt", "a") as file:
            file.write(schedule + "\n")

        write_log("logs/backup_manager.log", f"Schedule created: {schedule}")

    except Exception:
        write_log("logs/backup_manager.log", f"Error: malformed schedule: {schedule}")


def list_schedules():

    try:
        with open("backup_schedules.txt", "r") as file:

            lines = file.readlines()

            for i, line in enumerate(lines):
                print(f"{i}: {line.strip()}")

        write_log("logs/backup_manager.log", "Schedules listed")

    except Exception:
        write_log("logs/backup_manager.log", "Error: can't find backup_schedules.txt")


def delete_schedule(index):

    try:
        with open("backup_schedules.txt", "r") as file:
            lines = file.readlines()
            # Your task: check if index is invalid

        if index < 0 or index >= len(lines):
            write_log("logs/backup_manager.log", f"Error: invalid index: {index}")
            return
        lines.pop(index)

        with open("backup_schedules.txt", "w") as file:
            file.writelines(lines)
        write_log("logs/backup_manager.log", f"Schedule deleted: {index}")

    except Exception:
        write_log(
            "logs/backup_manager.log",
            f"Error: can't delete schedule with index: {index}",
        )


def is_service_running():
    try:
        # List all processes
        result = subprocess.run(
            ["ps", "-A", "-o", "pid,cmd"], stdout=subprocess.PIPE, text=True
        )
        for line in result.stdout.splitlines():
            if "backup_service.py" in line and "python" in line:
                return True
        return False
    except Exception:
        return False


def start_service():
    try:
        if is_service_running():
            write_log(
                "logs/backup_manager.log", "Error: backup_service already running"
            )
            return

        python_exec = sys.executable  # ensures we use the current Python interpreter
        subprocess.Popen(
            [python_exec, "backup_service.py"],
            start_new_session=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        write_log("logs/backup_manager.log", "Backup service started")

    except Exception as e:
        write_log("logs/backup_manager.log", f"Error: can't start backup service: {e}")


def stop_service():
    try:
        result = subprocess.run(
            ["ps", "-A", "-o", "pid,cmd"], stdout=subprocess.PIPE, text=True
        )

        stopped = False
        for line in result.stdout.splitlines():
            if "backup_service.py" in line and "python" in line:
                pid = int(line.strip().split()[0])
                os.kill(pid, signal.SIGTERM)
                stopped = True

        if stopped:
            write_log("logs/backup_manager.log", "Backup service stopped")
        else:
            write_log("logs/backup_manager.log", "Error: can't stop backup_service")

    except Exception:
        write_log("logs/backup_manager.log", "Error: can't stop backup_service")


def list_backups():
    try:
        if not os.path.exists("backups"):
            write_log("logs/backup_manager.log", "Error: can't find backups directory")
            return

        files = os.listdir("backups")
        backups = [f for f in files if f.endswith(".tar")]

        if backups:
            for f in backups:
                print(f)
        else:
            print("No backup files found.")

        write_log("logs/backup_manager.log", "Backups listed")

    except Exception as e:
        write_log("logs/backup_manager.log", f"Error listing backups: {e}")


# Initialize environment
init_environment()


# MAIN PROG.

if len(sys.argv) < 2:
    write_log("logs/backup_manager.log", "Error: No command provided")

else:

    command = sys.argv[1]

    if command == "create":

        if len(sys.argv) < 3:
            write_log("logs/backup_manager.log", "Error: malformed schedule")

        else:
            schedule = sys.argv[2]
            create_schedule(schedule)

    elif command == "list":

        list_schedules()
    elif command == "delete":

        if len(sys.argv) < 3:
            write_log("logs/backup_manager.log", "Error: no index provided")
        else:
            index = int(sys.argv[2])
            delete_schedule(index)
    elif command == "start":
        start_service()
    elif command == "stop":
        stop_service()
    elif command == "backups":
        list_backups()

    else:
        write_log("logs/backup_manager.log", "Error: unknown command")
