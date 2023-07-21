# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue} [!] Downloading and installing ADVPhishing..."
git clone https://github.com/Ignitetch/AdvPhishing.git
cd AdvPhishing/
chmod 777 *
./Linux-Setup.sh
echo "${green} Done ! [Launch ADVPhishing with ./AdvPhishing.sh"

