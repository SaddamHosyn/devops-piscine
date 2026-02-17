#!/bin/bash
find . -iregex '.*\.\(txt\)' -printf '%f\n'
