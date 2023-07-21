
# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue}[!] Installing WEF ..."

# installing gem !
gem install wpxf

# installing manually with git 

apt-get install build-essential patch -yy 
apt-get install ruby-dev zlib1g-dev liblzma-dev libsqlite3-dev -yy 
git clone https://github.com/rastating/wordpress-exploit-framework
echo "${green}[!] Installed . To run the script simple execute : sudo wpxf.rb"
