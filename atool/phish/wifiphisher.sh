# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue} [!] Downloading and installing Wifiphisher ..."
git clone https://github.com/wifiphisher/wifiphisher.git

cd wifiphisher

sudo python setup.py install
echo "${green} Done !"
