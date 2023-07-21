#!/bin/bash

# shellcheck disable=SC2034
# shellcheck disable=SC2155

export green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

echo "${green}[!] Installing Mega.nz"

wget https://mega.nz/linux/repo/xUbuntu_23.04/amd64/megasync-xUbuntu_23.04_amd64.deb
sudo dpkg -i megasync-xUbuntu_23.04_amd64.deb

echo "${blue}[!] Done"