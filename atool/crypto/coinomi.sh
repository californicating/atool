# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

echo "${blue} [!] Downloading Coinomi wallet [Version :1.3.0] "
wget https://storage.coinomi.com/binaries/desktop/coinomi-wallet-1.3.0-linux64.tar.gz

echo "${green}[!] Done "

