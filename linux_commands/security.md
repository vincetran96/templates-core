# SHA hash of text in Mac terminal
`echo -n zxcv | shasum -a 1`

# SHA hash of a text file in Mac terminal
Removing the trailing newline character at the end of file:

`perl -pe 'chomp if eof' filename | shasum -a 1`

# SHA hash of content of a text file in Mac terminal
# Ignore all newlines
`awk '{printf "%s", $0} END {printf ""}' filename | shasum -a 1`
