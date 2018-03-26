set -e

if [[ ! -z $1 ]]; then
  . /usr/local/bin/start.sh rqalpha run 
else
  . /usr/local/bin/start.sh rqalpha run $*
fi


