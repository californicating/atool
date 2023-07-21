#!/bin/bash

export yellow="$(tput setaf 3)"
export green="$(tput setaf 2)"

echo "${yellow}[!] Downloading Red-rabbit ..."
git clone https://github.com/ArkAngeL43/Red-Rabbit-V5 ; cd Red-Rabbit-V5 ; chmod +x ./INSTALL_RR5.sh ; ./INSTALL_RR5.sh
echo "${green}[!] Done ..."
