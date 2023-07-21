# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

echo "${blue} [!] Installing fondo"
sudo apt-get install meson && sudo apt-get install valca && sudo apt-get install libgranite-dev && sudo apt-get install libgtk-3-dev && apt-get install libjson-glib-dev && apt-get install libsoup2.4-dev
git clone https://github.com/calo001/fondo.git && cd fondo./app install-deps && ./app install
echo "${green}Done !"