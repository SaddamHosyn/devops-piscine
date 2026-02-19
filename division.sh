#!/bin/bash

if (( $# < 2 )); then
    echo "Error: two numbers must be provided"
    exit 1
fi

if ! echo "$1" | grep -qE '^-?[0-9]+$' || ! echo "$2" | grep -qE '^-?[0-9]+$'; then
    echo "Error: both arguments must be integers"
    exit 1
fi

if echo "$2" | grep -qE '^-?0+$'; then
    echo "Error: division by zero is not allowed"
    exit 1
fi

echo "$1 / $2" | bc
