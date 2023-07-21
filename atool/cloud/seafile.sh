#!/bin/bash

# shellcheck disable=SC2034
# shellcheck disable=SC2155

export green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

echo "${green}[!] Installing Seafile client"

sudo wget https://linux-clients.seafile.com/seafile.asc -O /usr/share/keyrings/seafile-keyring.asc
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/seafile-keyring.asc] https://linux-clients.seafile.com/seafile-deb/$(lsb_release -cs)/ stable main" | sudo tee /etc/apt/sources.list.d/seafile.list > /dev/null
sudo apt install -y seafile-gui

echo "${blue}[!] Done"