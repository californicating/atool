
# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

cd /root/

echo "${blue}[!] Installing Evil Limiter"
git clone https://github.com/bitbrute/evillimiter.git
cd evillimiter
sudo python3 setup.py install 
echo "${green}Done !"