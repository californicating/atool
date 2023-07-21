# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue}[!] Installing BinWalk  .."

python3 setup.py install
wget https://github.com/ReFirmLabs/binwalk/archive/master.zip
unzip master.zip
apt-get update -yy 
apt-get install python-lzma
apt install binwalk -yy

echo "${green}[!] Done . "