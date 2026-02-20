#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo "Error"
    exit 1
fi
if [[ ! $1 =~ ^[0-9]+$ ]]; then
    echo "Error"
    exit 1
fi
if [[ $1 -lt 1 ]] || [[ $1 -gt 5 ]]; then
    echo "Error"
      exit 1
fi
array=("red" "blue" "green" "white" "black")
echo ${array[$(( $1 - 1 ))]}
