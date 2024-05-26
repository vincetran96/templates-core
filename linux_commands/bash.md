# Run a command with conditions
- Log to a file
- Define a function
- If/else
- While loop
- Check empty string
- Check if a command is already running
```
#!/bin/bash
set -eo pipefail

log_dir=/data/anhtv/spellchecker/logs
exec >"${log_dir}/cronjob_$(date +'%Y-%m-%dT%H:%M:%S').log" 2>&1

string_can_be_empty=$1
THIS_SCRIPT_DIR=$(dirname "$0")
PROJECT_ROOT=$(realpath "${THIS_SCRIPT_DIR}/")

function check_command_running {
    is_running=$(ps aux | grep -v 'awk' | awk '/SOME_COMMAND.sh/ {print $1, $2, $11}')
    if [ ! -z "$is_running" ]; then
        return 1
    fi
    return 0
}

# If string_can_be_empty is explicitly provided, run that date (keep retrying if training is already running)
# Else, run yesterday
if [ ! -z "$string_can_be_empty" ]; then
    while true; do
        if check_command_running >/dev/null 2>&1; then
            echo ">>> $(date +'%Y-%m-%dT%H:%M:%S'): SOME_COMMAND: run date ${string_can_be_empty}"
            cd "$PROJECT_ROOT"
            bash SOME_COMMAND.sh "$string_can_be_empty"
            break
        else
            echo ">>> $(date +'%Y-%m-%dT%H:%M:%S'): SOME_COMMAND already running, retrying in 30s"
            sleep 30
        fi
    done
else
    if check_command_running >/dev/null 2>&1; then
        yesterday=$(date --date="1 days ago" +'%Y-%m-%d')
        echo ">>> $(date +'%Y-%m-%dT%H:%M:%S'): SOME_COMMAND: run date ${yesterday}"
        cd "$PROJECT_ROOT"
        bash SOME_COMMAND.sh "$yesterday"
    else
        echo ">>> $(date +'%Y-%m-%dT%H:%M:%S'): SOME_COMMAND already running, exiting"
        exit 1
    fi
fi
```
