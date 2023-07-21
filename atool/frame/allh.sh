
# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue}[!] Installing HackingTools Framework ...."
git clone https://github.com/mishakorzik/AllHackingTools

#cd to directory allhackingtools
cd AllHackingTools

#Start script to install system

bash Install.sh
echo "${green}Done !"

