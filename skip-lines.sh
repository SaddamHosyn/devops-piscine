#!/bin/bash
ls -l | sed '1d' | sed -n '1~2p'
