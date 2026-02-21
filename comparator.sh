#!/bin/bash
if [[ $# -lt 2 ]]; then
    echo "Error: The script only works with two arguments!"
    exit 1
fi
if [[ $# -gt 2 ]]; then
    echo "Error: The script only works with two arguments!"
    exit 1
fi
if [[ ! $1 =~ ^[0-9]+$ ]] || [[ ! $2 =~ ^[0-9]+$ ]]; then
    echo "Error: Only two numeric arguments are acceptable!"
    exit 1
fi
if  [[ $1 -eq $2 ]]; then
    echo "$1 = $2"
fi
if  [[ $1 -lt $2 ]]; then
    echo "$1 < $2"
fi
if  [[ $1 -gt $2 ]]; then
    echo "$1 > $2"
fi

