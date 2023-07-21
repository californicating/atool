#!/bin/bash

export yellow="$(tput setaf 3)"
export green="$(tput setaf 2)"

echo "${yellow}[!] Downloading Xattacker ..."
git clone https://github.com/Moham3dRiahi/XAttacker.git
echo "${green} Done  ! To launch XAttacker use the commands [ cd XAttacker && perl XAttacker.pl ]"
