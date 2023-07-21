# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue} [!] Downloading chkrootkit"
git clone https://github.com/Magentron/chkrootkit
cd chkrootkit
make sense 

echo "${green} Done !"
echo "${green}[!] To run chkrootkit simply go in the directory and execute : ./chkrootkit [in root mode ]"