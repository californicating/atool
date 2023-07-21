
# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

cd /root/

echo "${blue}[!] Installing Sqlmap"
wget https://raw.github.com/derv82/wifite/master/wifite.py
chmod +x wifite.py
echo "${green}Done !"