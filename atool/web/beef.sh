
# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"
export red="$(tput setaf 1)"
cd /root/

echo "${blue}[!] Installing BeeF Framework ....."

apt-get install ruby ruby-dev -yy 
apt-get install git -yy
git clone https://github.com/beefproject/beef
ls
cd beef 
./install 
sudo rm Gemfile.lock 
echo "${red}WARNING [!] If there is an error with the installation please visit :https://www.developsec.com/2018/06/22/installing-beef-on-ubuntu-18-04/"
echo "${red}WARNING [!] You can also visit : https://www.youtube.com/watch?v=hD_JRo7YPcg"

# in case installation from scratch fails , install from apt 

apt-get install beef-xss -yy 

echo "${green}Done !"
