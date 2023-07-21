# shellcheck disable=SC2034
# shellcheck disable=SC2155

export green="$(tput setaf 2)"
export blue="$(tput setaf 6)"

echo "${green} [!] Downloading and installing Xaamp ..."
wget https://sourceforge.net/projects/xampp/files/XAMPP%20Linux/8.2.4/xampp-linux-x64-8.2.4-0-installer.run
chmod 755 xampp-linux-x64-8.2.4-0-installer.run
sudo ./xampp-linux-x64-8.2.4-0-installer.run
echo "${blue} [!] Done "

