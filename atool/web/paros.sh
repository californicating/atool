
# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

cd /root/

echo "${blue}[!] Installing Paros ..."
apt-get install default-jre -yy 
apt-get install paros -yy 
apt-get install ruby -yy 
echo "${green}Done !"