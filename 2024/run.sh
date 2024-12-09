#!/bin/bash

if [[ $# -ne 2 ]]; then
    echo Usage: ./run.sh [day] [input-file]
    exit 1
fi

DAY=$1
INPUT=$2.txt

echo using $INPUT for day $DAY:
cat $DAY/$INPUT | python $DAY/sol.py
