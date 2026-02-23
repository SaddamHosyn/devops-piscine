#!/bin/bash

#######################################
# 1. Validate arguments
#######################################

# TODO: Check:
# - exactly 1 argument?
# - is it numeric?
# - is it between 1 and 100?
#
# If anything is wrong:
#   echo "Error: wrong argument"
#   exit 1



if [[ $# -ne 1 ]]; then
      echo "Error: wrong argument"
      exit 1
   
elif [[ ! $1 =~ ^[0-9]+$ ]]; then
      echo "Error: wrong argument"
      exit 1
elif [[ $1 -lt 1 || $1 -gt 100 ]]; then
      echo "Error: wrong argument"
      exit 1
fi
#######################################
# 2. Store the secret number
#######################################

# TODO: If validation passed, store $1 in a variable, e.g.:
# secret="$1"
    secret=$1








#######################################
# 3. Game loop (5 tries) using for
#######################################

# We need:
# - a for loop that runs from 1 to 5 (tries)
# - a variable to count how many valid attempts were used
#
valid_tries=0
for i in {1..5}; do
   tries_left=$(( 5 - valid_tries))
   echo "Enter your guess (${tries_left} tries left):"
   read guess
   valid_tries=$((valid_tries + 1))
   if [[ $guess -gt $secret ]]; then
      echo "Go down"
   elif [[ $guess -lt $secret ]]; then  # Use elif to match diff's single outputs [web:1]
      echo "Go up"
   else
      echo "Congratulations, you found the number in ${valid_tries} moves!"
      exit 0
   fi
done 







# For each iteration:
#   - calculate how many tries are left
#   - prompt: "Enter your guess (<tries_left> tries left):"
#   - read user input into a variable, e.g. guess
#   - check if guess is:
#       - empty → ask again (same tries_left, don't count this as a valid try)
#       - non-numeric → ask again (same tries_left, don't count this as a valid try)
#       - numeric → compare with secret

# Pseudocode for the loop structure:

# valid_tries=0
# for i in {1..5}; do
#   tries_left=$((5 - valid_tries))
#   echo "Enter your guess (${tries_left} tries left):"
#   read guess
#
#   # 3.1 validate guess (empty / non-numeric)
#   #   if invalid → continue without increasing valid_tries
#
#   # 3.2 if valid:
#   #   valid_tries=$((valid_tries + 1))
#   #   compare guess with secret:
#   #       if guess > secret → "Go down"
#   #       if guess < secret → "Go up"
#   #       if guess == secret:
#   #          print "Congratulations, you found the number in <valid_tries> moves!"
#   #          exit 0
# done


#######################################
# 4. If we reach here, player lost
#######################################

# TODO:
# echo "You lost, the number was $secret"


echo "You lost, the number was $secret"
