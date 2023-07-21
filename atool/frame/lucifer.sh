
# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue}[!] Installing Lucifer  Framework ...."
git clone https://github.com/Skiller9090/Lucifer.git
cd Lucifer
pip install -r requirements.txt
python main.py --help
echo "${green}Done !"


