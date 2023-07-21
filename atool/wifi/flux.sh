# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

cd /home/

echo "${blue} [!] Upgrading/installing packages and cloning repo "
sudo apt-get full-upgrade -yy
sudo apt-get install xdpyinfo -yy
sudo apt-get install mkd3 -yy
sudo apt-get install aircrack-ng -yy
sudo apt-get install bc -yy
sudo apt-get install hawk -yy
sudo apt-get install gawk -yy
sudo apt-get install curl -yy
sudo apt-get install cowpatty -yy
sudo apt-get install dhcpd -yy
sudo apt-get install 7zr -yy
sudo apt-get install hostapd -yy
sudo apt-get install lighttpd -yy
sudo apt-get install iwconfig -yy
sudo apt-get install macchanger -yy
sudo apt-get install mdk4 -yy
sudo apt-get install dnsiff -yy
sudo apt-get install nmap -yy
sudo apt-get install openssl -yy
sudo apt-get install php-cgi -yy
sudo apt-get install xtern -yy
sudo apt-get install rfkill -yy
sudo apt-get install unzip -yy
sudo apt-get install route -yy
sudo apt-get install fuser -yy
sudo apt-get install killall -yy
sudo apt-get install xdpyinfo -yy

git clone https://github.com/FluxionNetwork/fluxion
echo "${Magenta} [!] Done .."