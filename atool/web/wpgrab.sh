#!/bin/bash

export yellow="$(tput setaf 3)"
export green="$(tput setaf 2)"

echo "${yellow}[!] Downloading WpGrabInfo ..."
git clone https://github.com/Moham3dRiahi/WPGrabInfo
echo "${green} [!] Done , to run WpGrabInfo execute  the commands [ cd WPGrabInfo && perl WP-Grab.pl -u yourwebsite ] "
