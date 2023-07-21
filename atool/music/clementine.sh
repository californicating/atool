# shellcheck disable=SC2034
# shellcheck disable=SC2155

export blue="$(tput setaf 6)"
export green="$(tput setaf 2)"

echo "${green}[!] Installing Clementine"
sudo apt-get-repository ppa:me-davidsansome/Clementine
sudo apt-get update -yy
sudo apt-get install clementine -yy
echo "${blue}[!] Installed clementine"