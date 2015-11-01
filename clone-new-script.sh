#!/bin/bash

# Remove old repository
sudo rm -rf ~/cancer-project-ACC

cd 

# Download the new repository 
git clone https://github.com/JonasSam/cancer-project-ACC.git

# Kill previously started rabbitmq processes
sudo kill -9 `ps aux | grep erl | grep -v grep | awk '{print $2}'`

# Start the rabbitmq-server 
sudo rabbitmq-server &

