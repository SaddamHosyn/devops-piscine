#!/bin/bash

do_add() {
    echo "$(($1 + $2))"
}

do_sub() {
    echo "$(($1 - $2))"
}

do_mult() {
    echo "$(($1 * $2))"
}

do_divide() {
    echo "$(($1 / $2))"
}

# 1) Check number of arguments
if [[ $# -ne 3 ]]; then
    echo "Error: expect 3 arguments" >&2
    exit 1
fi

left="$1"
op="$2"
right="$3"

# 2) Check that both numbers are valid integers (allow negative)
if [[ ! $left =~ ^-?[0-9]+$ ]] || [[ ! $right =~ ^-?[0-9]+$ ]]; then
    echo "Error: invalid number" >&2
    exit 4
fi

# 3) Division by zero check (only matters for /)
if [[ "$op" == "/" && "$right" -eq 0 ]]; then
    echo "Error: division by 0" >&2
    exit 2
fi

# 4) Choose operation with case
case "$op" in
    "+")
        do_add "$left" "$right"
        ;;
    "-")
        do_sub "$left" "$right"
        ;;
    "*")
        do_mult "$left" "$right"
        ;;
    "/")
        do_divide "$left" "$right"
        ;;
    *)
        echo "Error: invalid operator" >&2
        exit 3
        ;;
esac
