#!/bin/bash

# shellcheck disable=SC1009
# shellcheck disable=SC2155
# shellcheck disable=SC2092
# shellcheck disable=SC2006

export red="$(tput setaf 1)"
export green="$(tput setaf 2)"
export yellow="$(tput setaf 3)"
export blue="$(tput setaf 4)"


banner(){

echo "${red}███████ ███████ ████████ ██    ██ ██████"
echo "${red}██      ██         ██    ██    ██ ██   ██"
echo "${red}███████ █████      ██    ██    ██ ██████"
echo "${red}     ██ ██         ██    ██    ██ ██"
echo "${red}███████ ███████    ██     ██████  ██"

}

check(){
  if [ "$(dpkg -l | awk '/snapd/ {print }'|wc -l)" -ge 1 ]; then
    echo "${blue}[!] Found snapd , continuing "
  fi
    echo "${blue}[!] Installing snap "
    sudo apt-get update -yy
    sudo apt-get install snapd
}

banner
check

# Update
sudo apt-get update -yy && sudo apt-get full-upgrade -yy


# Installing packages
apt-get install git -yy
apt-get install ssh -yy
apt-get install gnome-terminal -yy
apt-get intstall terminator -yy
apt install curl -yy
apt-get install gnome-tweaks -yy
apt-get install libmediainfo0v5 -yy && sudo apt-get install libzen0v5 -yy
apt-get install yt-dlp -yy
apt install gnome-shell-extension-prefs -yy
apt-get install git -yy && apt-get install ssh -yy && apt-get install gnome-terminal -yy && apt-get update -yy && apt-get full-upgrade -yy
apt-get install neofetch -yy
apt-get install fish -yy
apt-get install apache2 -yy
apt-get install net-tools

# Wine
dpkg --add-architecture i386 && apt-get update -yy && apt-get install wine32 -yy apt-get install wine64 -yy

# Installing telegram
sudo snap install telegram-desktop

# Installing discord
sudo apt-get install libgconf-2-4 libappindicator1 -yy
sudo snap install discord

# Installing vlc
sudo snap install vlc

#Installing Obs studio
sudo add-apt-repository ppa:obsproject/obs-studio
sudo apt install obs-studio

#Installing tor
sudo apt install torbrowser-launcher -yy

# Installing brave
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list
sudo apt update -yy
sudo apt install brave-browser -yy

# Installing google chrome
echo "${yellow}[+] Downloading and installing Google chrome "
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

# Installing mega.nz app
wget https://mega.nz/linux/repo/xUbuntu_23.04/amd64/megasync-xUbuntu_23.04_amd64.deb
sudo dpkg -i "megasync-xUbuntu_23.04_amd64.deb"

# Osintgram
git clone https://github.com/Datalux/Osintgram

# GOGH
sudo apt-get install dconf-cli uuid-runtime -yy
git clone https://github.com/Mayccoll/Gogh

# Installing code
sudo apt install software-properties-common apt-transport-https wget -yy
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
sudo apt-get  update && sudo apt-get install code -yy

# Installing pycharm community
sudo snap install pycharm-community --classic

# Installing spotify
curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg | sudo apt-key add -
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list
sudo apt-get update && sudo apt-get install spotify-client -yy
sudo snap install spotify


# Updating again
sudo apt-get update -yy && sudo apt-get full-upgrade -yy
sudo apt autoremove


changes(){

  # Change taskbar location (bottom)
  # Make icons smaller
  # gsettings set org.gnome.desktop.background picture-uri file:///home/serrano/Pictures/blank_image.jpg

  ID=$('/^ID=/' /etc/*-release | awk -F'=' '{ print tolower($2) }')
  LSB=$(lsb_release -i | cut -f 2-)
  clear

  if [ "$ID" == "ubuntu" ] || [ "$LSB" == "Ubuntu" ]; then
    gsettings set org.gnome.shell.extensions.dash-to-dock dock-position BOTTOM
    gsettings set org.gnome.shell.extensions.dash-to-dock dash-max-icon-size 30
    echo "${yellow}[!] Done"
  fi
}

changes
