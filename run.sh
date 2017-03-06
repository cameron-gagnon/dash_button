#!/bin/bash

# kill any previous instances of this process
ps aux | grep 'listen.py' | sudo kill $(awk '{print $2}')

# start a fresh instance
sudo nohup python listen.py &
