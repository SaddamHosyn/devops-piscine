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

for ((tries_left = 5; tries_left > 0; tries_left--)); do
    echo "Enter your guess ($tries_left tries left):"
    read guess

    if [[ -z "$guess" || ! "$guess" =~ ^[0-9]+$ || "$guess" -lt 1 || "$guess" -gt 100 ]]; then
        tries_left=$((tries_left + 1))  # Don't count invalid input
        continue
    fi

    if [[ "$guess" -eq "$secret" ]]; then
        echo "Congratulations, you found the number in $((6 - tries_left)) moves!"
        exit 0
    elif [[ "$guess" -lt "$secret" ]]; then
        echo "Go up"
    else
        echo "Go down"
    fi
done

#######################################
# 4. If we reach here, player lost
#######################################

echo "You lost, the number was $secret"
