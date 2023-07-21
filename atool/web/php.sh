# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

cd /root/
echo "${blue}[!] Installing phpsploit ..."
git clone https://github.com/nil0x42/phpsploit
cd phpsploit/
pip3 install -r requirements.txt
echo "${green}[!] Done ! .[To launch phpsploit execute : ./phpsploit]"