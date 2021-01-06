#!/bin/bash
# wait-for-postgres.sh

set -e
host="$1"
shift
cmd="$@"
echo "Waiting for mysql"
until mysqladmin ping -h pdb --silent; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
>&2 echo "Postgres is up - executing command"
exec $cmd