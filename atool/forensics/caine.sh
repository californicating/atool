# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"
export red="$(tput setaf 1)"


echo ""

while true; do
    read -p "${green}[!] Caine is an operating system and its size is approximately 2.9 GB . Do you want to download the iso file ? (y/n)" yn
    case $yn in
        [Yy]* ) wget http://caine.mirror.garr.it/mirrors/caine/caine7.0.iso ; break;;
        [Nn]* ) exit;;
        * ) echo "${red}[!] Please answer yes or no.";;
    esac
done

echo "${green}[!] Done !"
