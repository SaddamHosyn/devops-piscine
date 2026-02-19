#!/bin/bash
cat > show-info.sh << 'OUTER'
cat -e << EOF
The current directory is: $PWD
The default paths are: $PATH
The current user is: $USERNAME
EOF
OUTER
