# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "${blue} [!] Installing Mac-Location-Scraper"
git clone https://github.com/mac4n6/Mac-Locations-Scraper

echo "${green} Done !"

echo "${blue}
Usage:
python mac_locations_scraper.py -output {k, c, e} <directory_of_dbs>"
