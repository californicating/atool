# shellcheck disable=SC2034
# shellcheck disable=SC2155

export blue="$(tput setaf 6)"
export green="$(tput setaf 2)"

echo "${green}[!] Installing rhythmbox"
sudo add-apt-repository ppa:ubuntuhandbook1/apps
sudo apt-get update -yy
sudo apt-get install rhythmbox -yy
echo "${blue}[!] Installed rhythmbox"