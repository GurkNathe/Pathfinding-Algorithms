#!/bin/bash

# Check for missing commit message
if [ -z "$1" ]; then
    echo "Error: Please provide a commit message."
    exit 1
fi

# Enable extended globbing.
shopt -s extglob 
dir="main/testing/results"

if [ -d "$dir" ]; then
    file_count=$(ls -1 "$dir" | wc -l)
    if [ "$file_count" -gt 1 ]; then

        # Navigate to the subfolder containing the CSV files.
        cd "$dir"
        rm !(Generated_Maze-Example.csv)
        echo "Deleting CSV files from ./main/testing/results"
    fi
fi

# Upload to repository
git add -A
git commit -m "$1"
git push