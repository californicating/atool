# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

cd /root/

echo "${blue}[!] Installing required packages .."
apt-get install hostapd -yy && sudo apt-get install asleap -yy && sudo apt-get install crunch -yy && sudo apt-get install iptables -yy && sudo apt-get install hostpd-wpe -yy && sudo apt-get install dnsspoof -yy && sudo apt-get install reaver -yy && sudo apt-get install dhcpd -yy && sudo apt-get install isc-dhcp-server -yy && sudo apt-get install dhcp-server -yy && sudo apt-get install openssl -yy && sudo apt-get install wash -yy && sudo apt-get install pixiewps -yy && sudo apt-get install lighttpd -yy && sudo apt-get install beef-xss -yy && sudo apt-get install beef -yy && sudo apt-get install beef-project -yy && sudo apt-get install hostapd -yy && sudo apt-get install mdk4 -yy && sudo apt-get install ettercap -yy && sudo apt-get install bully -yy &&  sudo apt-get install aireplay-ng -yy && sudo apt-get install john -yy && sudo apt-get install wpaclean -yy && sudo apt-get install hashcat -yy && sudo apt-get install etterlog -yy && sudo apt-get install packetforge-ng -yy && sudo apt-get install bettercap -yy && sudo apt-get install ps -yy

echo "${blue} [!] Installing airgeddon"
git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git
cd airgeddon && ls
chmod 777 airgeddon.sh
echo "${green} Done !"