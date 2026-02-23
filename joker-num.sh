#!/bin/bash

#######################################
# 1. Validate arguments
#######################################

if [[ $# -ne 1 || -z "$1" || ! "$1" =~ ^[0-9]+$ || "$1" -lt 1 || "$1" -gt 100 ]]; then
    echo "Error: wrong argument"
    exit 1
fi

#######################################
# 2. Store the secret number
#######################################

secret="$1"

#######################################
# 3. Game loop (5 tries) using for
#######################################

valid_tries=0
while [[ $valid_tries -lt 5 ]]; do
    tries_left=$((5 - valid_tries))
    echo "Enter your guess (${tries_left} tries left):"
    read guess

    # Validate guess
    if [[ -z "$guess" || ! "$guess" =~ ^[0-9]+$ || "$guess" -lt 1 || "$guess" -gt 100 ]]; then
        continue  # invalid input, do not count as a try
    fi

    valid_tries=$((valid_tries + 1))
    if [[ "$guess" -gt "$secret" ]]; then
        echo "Go down"
    elif [[ "$guess" -lt "$secret" ]]; then
        echo "Go up"
    else
        echo "Congratulations, you found the number in ${valid_tries} moves!"
        exit 0
    fi
done

#######################################
# 4. If we reach here, player lost
#######################################

echo "You lost, the number was $secret"
