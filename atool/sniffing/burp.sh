# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"
export red="$(tput setaf 1)"


echo "${blue}[!] Installing Burpsuite......"
wget https://portswigger.net/burp/releases/download?product=community&version=2021.8.2&type=Linux

while true; do
    read -p "${green}[!] Do you wish to install this program? (y/n)" yn
    case $yn in
        [Yy]* ) sudo bash burpsuite_community_linux_v2021_8_2.sh ; break;;
        [Nn]* ) exit;;
        * ) echo "${red}Please answer yes or no.";;
    esac
done

echo "${green}[!] Done !"
