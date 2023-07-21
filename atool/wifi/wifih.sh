
# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

cd /root/

echo "${blue}[!] Installing Wifi-Hacking ...."
apt-get install aircrack-ng -yy 
git clone https://github.com/brannondorsey/wifi-cracking

echo "${green}[!] Downloading rockyou.txt"
curl -L -o rockyou.txt https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
echo "${green}Done !"




