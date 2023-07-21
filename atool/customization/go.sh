# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

echo "${blue} [!] Installing Gogh"
sudo apt-get install dconf-cli uuid-runtime -yy
git clone https://github.com/Mayccoll/Gogh
echo "${green} Done"