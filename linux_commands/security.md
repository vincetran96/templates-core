# SHA hash of text in Mac terminal
`echo -n zxcv | shasum -a 1`

# SHA hash of content of a text file in Mac terminal
# Ignore all newlines
`awk '{printf "%s", $0} END {printf ""}' filename | shasum -a 1`
