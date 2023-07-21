# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue} [!] Downloading and installing Hidden Eye"
git clone https://github.com/DarkSecDevelopers/HiddenEye-Legacy
chmod 777 HiddenEye
sudo apt install python3-pip -yy
cd HiddenEye
sudo pip3 install -r requirements.txt
sudo pip3 install requests
sudo pip3 install pyngrok
echo "${green} Done ! [To run execute : python3 HiddenEye.py]"
