# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

echo "${blue} [!] Downloading Exodus wallet [version : 23.7.17]"
wget https://downloads.exodus.com/releases/exodus-linux-x64-23.7.17.deb
dpkg -i exodus-linux-x64-23.7.17.deb
echo "${green}[!] Done "

