# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

echo "${blue} [!] Downloading Osinted"
git clone https://github.com/SpookySec/OSINTed
echo "${green} Done ! "