# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue}[!] Installing Recon-ng"
git clone https://github.com/lanmaster53/recon-ng
echo "${green}Done !"



