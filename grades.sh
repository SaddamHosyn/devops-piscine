#!/bin/bash
# grades.sh template - Follow each step in order

# STEP 1: Check if exactly 1 argument is provided
# Hint: Use $# and if statement with test condition for argument count
# Print error to stderr using 1>&2 and exit 1

if [[ $# -ne 1 ]]; then
    echo "Error: wrong argument" >&2
    exit 1
fi


# STEP 2: Extract number of students from first argument
# Hint: Store $1 in a variable, validate it's a positive integer

student_count="$1"

if [[ ! "$student_count" =~ ^[0-9]+$ ]] || [[ "$student_count" -lt 1 ]]; then
    echo "Error: wrong argument" >&2
    exit 1
fi



# STEP 3: Initialize counters for student loop
# Hint: Use a for loop with sequence from 1 to number of students

for ((i = 1; i <= student_count; i++)); do
    
    read -p "Student Name #$i: " name
      read -p "Student Grade #$i: " grade

   if [[ ! "$name" =~ ^[a-zA-Z]+$ ]]; then
        echo "Error: wrong argument" >&2
        exit 1
    fi

      if [[ ! "$grade" =~ ^[0-9]+$ ]] || [[ "$grade" -lt 0 || "$grade" -gt 100 ]]; then
    echo "Error: wrong argument" >&2
    exit 1
fi


if [[ "$grade" -ge 90 ]]; then
    evaluation="$name: You did an excellent job!"
elif [[ "$grade" -ge 70 ]]; then
    evaluation="$name: You did a good job!"
elif [[ "$grade" -ge 50 ]]; then
    evaluation="$name: You need a bit more effort!"
else
    evaluation="$name: You had a poor performance!"
fi


echo "$evaluation"
done






# STEP 4: Inside the student loop - Prompt and read student name
# Hint: Use read -p with numbered prompt "Student Name #X: "

# STEP 5: Inside the student loop - Prompt and read student grade
# Hint: Use read -p with numbered prompt "Student Grade #X: "

# STEP 6: Validate grade input
# Hint: Check if grade is numeric using [[ $grade =~ ^[0-9]+$ ]]
# Check range 0-100 inclusive
# If invalid: Print error to stderr with exact message format, exit 1


# STEP 7: Determine evaluation message based on grade ranges
# Hint: Use nested if-elif-else statements
# >=90: "<name>: You did an excellent job!"
# >=70: "<name>: You did a good job!" 
# >=50: "<name>: You need a bit more effort!"
# <50:  "<name>: You had a poor performance!"



# STEP 8: Print the evaluation message
# Hint: echo the message immediately after grade evaluation


# END: Script completes after all students processed
