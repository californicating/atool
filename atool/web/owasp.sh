
# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

cd /root/

echo "${blue}[!] Installing Zaproxy......"
wget https://github.com/zaproxy/zaproxy/releases/download/v2.10.0/ZAP_2_10_0_unix.sh

while true; do
    read -p "${green}[!] Do you wish to install this program? (y/n)" yn
    case $yn in
        [Yy]* ) sudo bash ZAP_2_10_0_unix.sh ; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

echo "${green}[!] Done !"

