
# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue}[!] Installing BlackTool Framework ...."
git clone https://github.com/mrprogrammer2938/Black-Tool
cd Black-Tool
python3 install.py


echo "${green}Done ![To launch hacking tool , execute :python3 hack --start ] "
echo "${green}[!] To update script execute: cd Update , ./update "
