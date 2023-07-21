# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

echo "${blue} [!] Installing Sublime text editor "
sudo apt-get install gdebi -yy
wget https://download.sublimetext.com/sublime-text_build-3211_amd64.deb
sudo dpkg -i  sublime-text_build-3211_amd64.deb
echo "${green} Done ! "
