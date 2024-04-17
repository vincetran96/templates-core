# Find if a process is running based on name
`ps aux | grep -v 'awk' | awk '/process_name/ {print $1, $2, $11}'`
