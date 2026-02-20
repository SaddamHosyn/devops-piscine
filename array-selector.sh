#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo "Error"

fi
if [[ ! $1 =~ ^[0-9]+$ ]]; then
 
fi
if [[ $1 -lt 1 ]] || [[ $1 -gt 5 ]]; then
    echo "Error"

fi
array=("red" "blue" "green" "white" "black")
echo ${array[$(( $1 - 1 ))]}
