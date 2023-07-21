# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue} [!] Downloading Tools-Phishing ..."
git clone https://github.com/AdrMXR/tools-phishing.git
echo "${green} Done ! [To run Tools-Phishing execute : python tools-phishing.py ]"
