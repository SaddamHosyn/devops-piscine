#!/bin/bash
ls -tup | tr '\n' ',' | sed 's/,$//'
