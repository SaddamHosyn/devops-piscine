def to_do(tasks):
    with open("output.txt", "w", encoding="utf-8") as f:
        for date_obj, task in tasks:
            # Format date as "Weekday DD Month YYYY"
            formatted_date = date_obj.strftime("%A %d %B %Y")
            # Write to file with task
            f.write(f"{formatted_date}: {task}\n")
