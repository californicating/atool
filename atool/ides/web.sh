# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

echo "${blue} [!] Installing WebStorm "
wget https://download.jetbrains.com/webstorm/WebStorm-2021.1.2.tar.gz
sudo tar xzf WebStorm-2021.1.2.tar.gz -C /opt
/opt/WebStorm-211.7442.26/bin/webstorm.sh

