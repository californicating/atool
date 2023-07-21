# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "[!] Installing dnmap"
git clone https://github.com/darkoperator/dnsrecon
echo "${green}Done !"
