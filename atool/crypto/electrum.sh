# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

echo "${blue} [!] Downloading Electrum wallet "
sudo apt install python3-setuptools python3-pyqt5 python3-pip -yy
wget https://download.electrum.org/4.4.5/electrum-4.4.5-x86_64.AppImage
echo "${green}[!] Done "

