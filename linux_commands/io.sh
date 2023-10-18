#!bin/bash

# Delete all __pycache__ dirs recursively in current dir
find . -type d -name "__pycache__" -exec rm -r {} +
