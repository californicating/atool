# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue} [!] Downloading Zphisher .... "
git clone git://github.com/htr-tech/zphisher.git
echo "${green} Done ! [To run Lordphish execute : bash zphisher.sh]"

