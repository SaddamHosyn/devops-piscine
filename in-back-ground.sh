#!/bin/bash
nohup sh -c 'cat facts | grep "moon" && echo "The moon fact was found!" >> output.txt' > /dev/tty 2>&1 &
wait
