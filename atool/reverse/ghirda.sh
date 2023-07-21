#!/bin/bash

# shellcheck disable=SC2242


export yellow="$(tput setaf 3)"
export red="$(tput setaf 1)"
export green="$(tput setaf 2)"
export blue="$(tput setaf 4)"

echo "${yellow}[!] Downloading Ghirda ..."

wget https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.3.2_build/ghidra_10.3.2_PUBLIC_20230711.zip
unzip ghidra_10.3.2_PUBLIC_20230711.zip

cd ghidra_10.3.2_PUBLIC

apt-get install default-jdk -yy 
echo ""

while true; do
    read -p "${green}[!] Do you want to launch Ghirda now (y/n) ? " yn
    case $yn in
        [Yy]* ) ./ghidraRun ; break;;
        [Nn]* ) exit "[!] If you want to run ghirda go inside the directory and run : ./ghirdaRun ";;
        * ) echo "${red}[!] Please answer yes or no.";;
    esac
done


