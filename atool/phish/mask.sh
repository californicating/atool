# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue} [!] Downloading Maskphish ... "
git clone https://github.com/jaykali/maskphish
echo "${green} Done ! [To run maskphish, execute :bash maskphish.sh]"
