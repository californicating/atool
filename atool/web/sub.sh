#!/bin/bash

export yellow="$(tput setaf 3)"
export green="$(tput setaf 2)"

echo "${yellow}[!] Downloading Subscan ..."
git clone https://github.com/C043R/SubScan
cd SubScan
sudo bash setup.sh
echo "${green} [!] Done ,run SubScan with : sudo python3 scan.py "