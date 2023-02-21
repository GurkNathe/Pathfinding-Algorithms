#!/bin/bash

# Check for missing commit message
if [ -z "$1" ]; then
    echo "Error: Please provide a commit message."
    exit 1
fi

# Enable extended globbing.
shopt -s extglob 

# Navigate to the subfolder containing the CSV files.
cd main/testing/results  
rm !(Generated_Maze-Example.csv)

# Upload to repository
git add -A
git commit -m "$1"
git push