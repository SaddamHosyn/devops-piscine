#!/bin/bash
sleep 3 &
sleep 5 &
sleep 7 &
jobs -l | awk '{print $1, $3, $4, $5, $6}'
