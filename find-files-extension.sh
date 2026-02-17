#!/bin/bash
find . -iregex '.*\.\(txt\)' | cut -d '/' -f 3
