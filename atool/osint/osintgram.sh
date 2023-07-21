# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue} [!] Downloading Osintgram"
git clone https://github.com/Datalux/Osintgram
echo "${green} Done ! "
