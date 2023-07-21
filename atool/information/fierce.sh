
# shellcheck disable=SC2034
# shellcheck disable=SC2155

export  green="$(tput setaf 2)"
export blue="$(tput setaf 6)"


echo "[!] Installing fierce "
git clone https://github.com/mschwager/fierce
cd fierce 
python -m pip install -r requirements.txt
python fierce/fierce.py -h
echo "${green}Done !"
