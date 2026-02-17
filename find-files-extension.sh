#!/bin/bash
find . -iregex '.*\.\(txt\)' -printf '%f\n' | cut -d '.' -f 1
