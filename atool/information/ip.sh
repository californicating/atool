#!/bin/bash

export yellow="$(tput setaf 3)"
export green="$(tput setaf 2)"

echo "${yellow}[!] Downloading Iptracker ..."

git clone https://github.com/anonymousproo/IP-Tracker.git
cd IP-Tracker
chmod +x IP-Tracker.py
