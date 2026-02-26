import sys
import os

# Check for exactly one argument (script name + filename)
if len(sys.argv) != 2:
    exit(1)

file_name = sys.argv[1]

# Check if file exists and is readable
if not os.path.isfile(file_name) or not os.access(file_name, os.R_OK):
    exit(1)

try:
    with open(file_name, "r", encoding="utf-8") as f_in, open("out.txt", "w", encoding="utf-8") as f_out:
        for line in f_in:
            # Skip lines containing the word "pineapple"
            if "pineapple" not in line:
                f_out.write(line)
except Exception:
    exit(1)
