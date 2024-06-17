# Delete all __pycache__ dirs recursively in current dir
`find . -type d -name "__pycache__" -exec rm -r {} +`

# Show disk usage of dirs (?) at the top level in current dir
`du -hd1 | sort -h`

# Tar
## Extract an archive (tgz) to directory
`tar xzf path/to/target.tar.gz --directory=path/to/directory`
