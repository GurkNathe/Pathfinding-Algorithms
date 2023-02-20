if [ -z "$1" ]; then
    echo "Error: Please provide a commit message."
    exit 1
fi

git add -A
git commit -m "$1"
git push