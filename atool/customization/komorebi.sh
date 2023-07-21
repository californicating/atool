# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

echo "${green}Installing required packages and downloading Komorebi"
sudo apt install cmake -yy
sudo apt-get install build-essential -yy
sudo add-apt-repository ppa:gnome3-team/gnome3
sudo add-apt-repository ppa:vala-team
sudo add-apt-repository ppa:gnome3-team/gnome3-staging
sudo apt install cmake -yy
sudo valac -yy
sudo libgtk-3-dev -yy
sudo libgee-0.8-dev -yy
sudo libclutter-gtk-1.0-dev -yy
sudo libclutter-1.0-dev -yy
sudo libwebkit2gtk-4.0-dev -yy
sudo libclutter-gst-3.0-dev -yy
git clone https://github.com/cheesecakeufo/komorebi.git
cd komorebi
mkdir build && cd build
cmake .. && sudo make install
echo "${blue}Installed Komorebi!"