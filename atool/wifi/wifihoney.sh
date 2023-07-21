
# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

cd /root/

echo "${blue}[!] Installing Wifi Honey"
git clone https://github.com/samothrakes/wifi-honey.git
cd wifi-honey
chmod a+x wifi_honey.sh
echo "${green}Done !"