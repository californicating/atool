# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue} [!] Installing Volatolity "
sudo apt install git
git clone https://github.com/volatilityfoundation/volatility.git
cd volatility
chmod +x volatility/vol.py

echo "${green} Done !"
