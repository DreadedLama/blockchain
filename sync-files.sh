#!/bin/bash

port=$1

if [ -z "$port" ] #if port isn't assigned
then
  echo Need to specify port number
  exit 1
fi

FILES=(block.py chain.py mining.py server.py)

mkdir jbc$port
for file in "${FILES[@]}"
do
  echo Syncing $file
  ln ~/blockchain/$file blockchain$port/$file
done

echo Synced new folder for port $port

exit 1