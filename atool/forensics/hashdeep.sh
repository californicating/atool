# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue} [!] Installing HashDeep"

git clone https://github.com/jessek/hashdeep 

cd hashdeep
sh bootstrap.sh
./configure
make
make install

echo "${green} Done !"
