# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

echo "${blue} [!] Downloading and installing GoPhish"
git clone https://github.com/gophish/gophish
cd gophish && cd gophish && go build
echo "${green} Done !"