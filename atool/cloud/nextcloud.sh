#!/bin/bash

# shellcheck disable=SC2034
# shellcheck disable=SC2155

export green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

echo "${green}[!] Installing Nextcloud"

wget https://github.com/nextcloud-releases/desktop/releases/download/v3.9.0/Nextcloud-3.9.0-x86_64.AppImage
sudo apt install apache2 mariadb-server libapache2-mod-php7.4
sudo apt install php7.4-gd php7.4-mysql php7.4-curl php7.4-mbstring php7.4-intl
sudo apt install php7.4-gmp php7.4-bcmath php-imagick php7.4-xml php7.4-zip

echo "${blue}[!] Done"
