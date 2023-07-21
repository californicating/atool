
# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue}[!] Installing HackingTool Framework ...."
git clone https://github.com/Z4nzu/hackingtool.git
chmod -R 755 hackingtool  
cd hackingtool
sudo pip3 install -r requirement.txt
bash install.sh
echo "${green}Done ![To launch hacking tool , execute :sudo hackingtool ] "

