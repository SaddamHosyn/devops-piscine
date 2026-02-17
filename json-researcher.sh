#!/bin/bash
curl -s https://01.gritlab.ax/assets/superhero/all.json | jq '.[] | select(.id == 1)' | grep -E '"name"|"power"'
