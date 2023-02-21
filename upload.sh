#!/bin/bash

if [ -z "$1" ]; then
    echo "Error: Please provide a commit message."
    exit 1
fi

shopt -s extglob # enable extended globbing

cd main/testing/results  # navigate to the subfolder containing the CSV files
rm !(Generated_Maze-Example.csv)

git add -A
git commit -m "$1"
git push