#!/bin/sh

echo "Killing previous dash_button/listen.py processes"
# kill any previous instances of this process
ps aux | grep 'listen.py' | tee /dev/tty | sudo kill $(awk '{print $2}')

echo "\nStarting dash_button/listen.py..."
# start a fresh instance
nohup sudo python listen.py &
sleep 0.2

echo "\n"
