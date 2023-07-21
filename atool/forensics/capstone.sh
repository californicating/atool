# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue} [!] Installing capstone"
apt-get install git && git clone git://git.kali.org/packages/capstone.git

echo "${green} Done !"