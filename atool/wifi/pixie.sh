
# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

cd /root/

echo "${blue}[!] Installing Sqlmap"
wget https://github.com/wiire/pixiewps/archive/master.zip && unzip master.zip
cd pixiewps*/
make
sudo make install
echo "${green}Done !"




