#!/bin/bash

# Check for missing commit message
if [ -z "$1" ]; then
    echo "Error: Please provide a commit message."
    exit 1
fi

# Enable extended globbing.
shopt -s extglob 

dir="main/testing/results"

# Check if directory exists
if [ -d "$dir" ]; then
    # Check if there are more than one file in the directory
    if [ "$(ls -1 "$dir" | wc -l)" -gt 1 ]; then
        # Navigate to the subfolder containing the CSV files.
        cd "$dir"
        rm !(Generated_Maze-Example.csv)

        echo "Deleting CSV files from ./main/testing/results"
    else
        echo "Directory contains only one file. Nothing deleted."
    fi
else
    echo "Directory does not exist."
fi

# Upload to repository
git add -A
git commit -m "$1"
git push
