set -e

# change work 
cd ~/work

# Exec the specified command or fall back on bash

if [ $# -eq 0 ]; then
    cmd=bash
else
    cmd=$*
fi

echo "Executing the command: $cmd"
exec $cmd
