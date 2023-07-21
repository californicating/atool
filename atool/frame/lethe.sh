
# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue}[!] Installing Lethe Framework ...."
git clone https://github.com/hades921/Lethe.git
cd Lethe
pip3 install -r requirements.txt

echo "${green}Done ! [To run Lethe Framework execute : python3 lethe.py ]"


