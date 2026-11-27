#!/bin/sh
# Copy the tracked pre-commit hook into this clone.
root=$(git rev-parse --show-toplevel) || exit 1
cd "$root" || exit 1
mkdir -p .git/hooks
cp scripts/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
echo "Installed .git/hooks/pre-commit"
