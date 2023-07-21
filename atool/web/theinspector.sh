#!/bin/bash

export yellow="$(tput setaf 3)"
export green="$(tput setaf 2)"

echo "${yellow}[!] Downloading Th3inspector ..."

git clone https://github.com/Moham3dRiahi/Th3inspector.git
cd Th3inspector
chmod +x install.sh && ./install.sh

echo "${green}[!] Done ,to run theinspector execute the commands [ cd Th3inspector && perl Th3inspector.pl -h" 
