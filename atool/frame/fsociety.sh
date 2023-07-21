
# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue}[!] Installing Fsociety Framework ...."
git clone https://github.com/Manisso/fsociety
bash install.sh

echo "${green}Done ![To launch hacking tool , execute : python3 fsociety.py ] "


