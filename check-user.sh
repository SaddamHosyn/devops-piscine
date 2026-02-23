#!/bin/bash

# 1. Check argument count
if [[ $# -ne 2 ]]; then
    echo "Error: expect 2 arguments" >&2
    exit 1
fi

# 2. Store arguments
flag="$1"
username="$2"

# 3. Validate flag
if [[ "$flag" != "-e" && "$flag" != "-i" ]]; then
    echo "Error: unknown flag" >&2
    exit 1
fi

# 4. Get user info
userinfo=$(getent passwd "$username")

# 5. Handle -e
if [[ "$flag" == "-e" ]]; then
    if [[ -n "$userinfo" ]]; then
        echo yes
    else
        echo no
    fi
    exit 0
fi

# 6. Handle -i
if [[ "$flag" == "-i" ]]; then
    if [[ -n "$userinfo" ]]; then
        echo "$userinfo"
    fi
    exit 0
fi
