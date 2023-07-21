# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue} [!] Installing Sleuth-kit .."

echo "${blue} Installing modules ! "
apt-get install g++ -yy && apt-get install jre -yy && apt-get install python -yy && apt-get install perl && apt-get install ruby -yy
apt-get install libssl-dev -yy 
apt-get isntall openssl-devel -yy 


echo "${blue} [!] Fetching Sleuth kit.zip"
wget https://github.com/sleuthkit/sleuthkit/archive/refs/tags/sleuthkit-4.11.0.zip

echo "${blue}[!] Unziping package ..."
unzip sleuthkit-4.11.0.zip

echo "${blue} [!] Getting afflib from github ..."
wget https://github.com/downloads/simsong/AFFLIBv3/afflib-3.7.1.tar.gz
tar -xvf afflib-3.7.1.tar.gz
cd afflib-3.7.1/
bash bootstrap
./configure
make 
sudo make install

echo "${blue} [!] Compiling sleuthkit.."
cd sleuthkit-sleuthkit-4.11.0/
bash bootstrap
./configure

echo "${green} Done !"
