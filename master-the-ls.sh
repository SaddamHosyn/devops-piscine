#!/bin/bash
ls -tupl | tr '\n' ',' | sed 's/,$//'
