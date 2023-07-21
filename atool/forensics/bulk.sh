
# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue}[!] Installing Bulk Extractor  .."
apt-get install git
git clone --recursive https://github.com/simsong/bulk_extractor.git
cd bulk_extractor
bash etc/CONFIGURE_UBUNTU20.bash
bootstrap.sh
./configure
echo "${green}[!] Compiling might take a while [ DO NOT INTERRUPT !]"
sleep 3 
make && sudo make install

echo "${green}[!] Done . "

