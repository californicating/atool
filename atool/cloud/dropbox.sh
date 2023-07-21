#!/bin/bash

# shellcheck disable=SC2034
# shellcheck disable=SC2155

export green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

echo "${green}[!] Installing Dropbox"

wget https://www.dropbox.com/download?dl=packages/ubuntu/dropbox_2022.12.05_amd64.deb
dpkg -i dropbox_2022.12.05_amd64.deb

echo "${blue}[!] Done"
