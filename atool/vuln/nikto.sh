
# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue}[!] Downloading Nikto"
git clone https://github.com/sullo/nikto
apt-get install nikto -yy
echo "${green}Done !"
