#!/bin/bash
# shellcheck disable=SC1009
# shellcheck disable=SC2155
# shellcheck disable=SC2092
# shellcheck disable=SC2006

export Red="$(tput setaf 1)"
export green="$(tput setaf 2)"
export yellow="$(tput setaf 3)"
export blue="$(tput setaf 4)"

if [ "$(id -u)" != "0" ]; then
  echo "${Red} [!] This script requires root privilege [run with : sudo bash setup.sh] "
  exit 1
fi

echo "${yellow}[!] Running installation script . Do not interrupt the process [!]"

apt-get install python3 
pip install python-dotenv
pip install urllib3
apt-get install python3-pip -yy
apt-get install git -yy 

check(){
  if [ "$(dpkg -l | awk '/snapd/ {print }'|wc -l)" -ge 1 ]; then 
  echo "${blue}[!] Found snapd , continuing "
else
  ID=$('/^ID=/' /etc/*-release | awk -F'=' '{ print tolower($2) }')
  LSB=$(lsb_release -i | cut -f 2-)
  clear
  echo "${green}[!] Installing required packages"
  if [ "$ID" == "kali" ] || [ "$LSB" == "Kali" ]; then
  apt-get update -yy
  apt-get install snapd
  echo "${yellow}[!] Done"
  fi

  if [ "$ID" == "parrot" ] || [ "$LSB" == "parrot" ]; then
  apt-get update -yy
  apt-get install snapd
  echo "${yellow}[!] Done"
  fi

  if [ "$ID" == "ubuntu" ] || [ "$LSB" == "Ubuntu" ]; then
  apt-get update -yy
  apt-get install snapd
  echo "${yellow}[!] Done"
  fi

  if [ "$ID" == "debian" ] || [ "$LSB" == "debian" ]; then
  apt-get update -yy
  apt-get install snapd
  echo "${yellow}[!] Done "

  else
  echo "${Red}[!] Detected unknown system , can't install snapd , therefore the program will exit"
  echo "${Red}[!] Supported systems : Ubuntu , Parrot os , Debian, Kali linux"
  sleep 2
  exit
  fi
  fi
}

check
