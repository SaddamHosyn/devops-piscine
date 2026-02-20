#!/bin/bash
if [[ $# -ne 1 ]] || [[ ! -d $1 ]]; then
    echo "Error"
    exit 1
fi
touch "$1/ciao"
chmod 442 "$1/ciao"
touch -t 200101010001 "$1/ciao"
mkdir "$1/mamma"
chmod 777 "$1/mamma"
touch -t 200101020001 "$1/mamma"
touch "$1/guarda"
chmod 400 "$1/guarda"
touch -t 200101030001 "$1/guarda"
touch "$1/come"
chmod 642 "$1/come"
touch -t 200101040001 "$1/come"
mkdir "$1/mi"
chmod 452 "$1/mi"
touch -t 200101050001 "$1/mi"
touch "$1/diverto"
chmod 421 "$1/diverto"
touch -t 200101060001 "$1/diverto"
