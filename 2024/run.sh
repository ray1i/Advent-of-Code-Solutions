#!/bin/bash

if [ $# -lt 2 ]; then
    echo "Usage: $0 <day> <input-files...>"
    exit 1
fi

DAY=$1
INPUT=$2.txt

echo using $INPUT for day $DAY:
cat $DAY/$INPUT | python $DAY/sol.py
