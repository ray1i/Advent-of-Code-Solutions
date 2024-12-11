#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Usage: $0 <day>"
    exit 1
fi

DAY=$1

if [ -d $DAY ]; then
    echo "$PWD/$DAY already exists, overwrite? (y/n)"
    read -r response
    if [ "$response" != "y" ]; then
        echo "aborting..."
        exit
    fi
fi

if rm -r ./$DAY; then
    echo "removed existing ./$DAY"
fi

mkdir $DAY
cp -r template/. $DAY

echo "done."


