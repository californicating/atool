#!/usr/bin/python3

import os
import platform
import time


class Colors:
    fgRed = "\033[31m"
    fgGreen = "\033[32m"
    fgYellow = "\033[33m"
    fgBlue = "\033[34m"
    fgMagenta = "\033[35m"
    fgCyan = "\033[36m"
    fgWhite = "\033[37m"


try:
    from urllib.request import urlopen
    import urllib
except ImportError or ModuleNotFoundError:
    question = input(Colors.fgRed + "[Error: missing modules] Run setup file ? (y/n)")
    if question == "y":
        print(Colors.fgGreen + "[!] Running setup.sh")
        os.system("bash setup.sh")
    elif question == "n":
        print(Colors.fgRed + "[!] Exiting...")
        exit(0)


if platform.system() != "Linux":
    print(Colors.fgRed+"[!] Sorry this tool is supported for Linux only")
    exit(0)
else:
    if os.geteuid() != 0:
        exit(Colors.fgRed+"[!] Detected linux but you need root privileges to run this script.")


def connection():
    try:
        urlopen('https://google.com', timeout=2)
        return True
    except urllib.error.URLError as Error:
        return False


if connection():
    print(Colors.fgBlue + "Connected to the internet " + Colors.fgBlue + "[" + Colors.fgGreen + '\u2713' + Colors.fgBlue + "]")
else:
    print(Colors.fgRed + "[!] Make sure you are connected to the internet . Exiting !")
    exit(0)


def banner():
    print(Colors.fgRed + """

 ____    _____ ____ ____ _ 
/  _ \  /__ __/  _ /  _ / \-
| / \_____/ \ | / \| / \| |
| |-|\____| | | \_/| \_/| |_/\-
\_/ \|    \_/ \____\____\____/

""")


def menu():
    banner()
    print(Colors.fgWhite + "1" + Colors.fgCyan + ") " + Colors.fgWhite + "Install python modules")
    print(Colors.fgWhite + "2" + Colors.fgCyan + ") " + Colors.fgWhite + "View Categories")
    print(Colors.fgWhite + "3" + Colors.fgCyan + ") " + Colors.fgWhite + "Update && Upgrade")
    print(Colors.fgWhite + "4" + Colors.fgCyan + ") " + Colors.fgWhite + "Popular apps")
    print(Colors.fgWhite + "5" + Colors.fgCyan + ") " + Colors.fgWhite + "Fast setup")
    print(Colors.fgWhite + "6" + Colors.fgCyan + ") " + Colors.fgWhite + "Help")
    print(Colors.fgWhite + "7" + Colors.fgCyan + ") " + Colors.fgWhite + "Exit")
    print("")

    choice = input(Colors.fgWhite + "[*]" + Colors.fgCyan + " Enter your choice > ")

    if choice == "1":
        def python_libs():
            print(Colors.fgCyan + """
                =========================================
                ***************** Options ***************
                
                1) List      
                2) Manual installation
                3) Go back
                4) Exit
                
                =========================================
                """)

            library_categories = input(Colors.fgWhite + "[!] Choose a category > ")

            if library_categories == "1":
                def lst():
                    print(Colors.fgCyan + f"""
                        ===================================================
                        ******************* Libraries *********************
                        
                        {Colors.fgRed}AI                         Editing/Processing{Colors.fgCyan}    
                                        
                        1) opencv-python             14) MoviePy
                        2) pandas                    15) Scikit-video
                        3) SciPy                     16) VidGear
                        4) Numpy                     17) Mahotas
                        5) PyTorch                   18) Pillow/PIL
                        6) Matplotlib                19) SimpleITK
                        7) Pytesseract               20) Pgmagick
                        8) Theano                    21) SimpleCV
                        9) TensorFlow
                        10) Keras
                        11) Seaborn
                        12) Scikit-Learn
                        13) Plotly

                        {Colors.fgRed}System                    Automation{Colors.fgCyan} 
                        22) psutil                31) selenium
                        23) ctypes                32) bs4
                        24) codecs                33) PyAutoGUI
                        25) paramiko              34) Pywinauto
                        26) logging               35) Requests
                        27) SaltStack             36) Watchdog
                        28) ansible               37) CSV
                        29) fabric                38) Splinter
                        30) pywin32               39) PyTest
                        
                        {Colors.fgRed}Api's                      {Colors.fgCyan}45) Go back
                        40) discord                46) Exit
                        41) nextcord
                        42) instagrapi
                        43) instagram_private_api
                        44) telegram
                        
                        ===================================================
                        """)

                    list_option = input(Colors.fgWhite + "[*]" + Colors.fgCyan + " Choose a category > ")

                    if list_option == "1":
                        os.system("pip install opencv-python")
                    elif list_option == "2":
                        os.system("pip install pandas")
                    elif list_option == "3":
                        os.system("pip install scipy")
                    elif list_option == "4":
                        os.system("pip install numpy")
                    elif list_option == "5":
                        os.system("pip install torch")
                    elif list_option == "6":
                        os.system("pip install matplotlib")
                    elif list_option == "7":
                        os.system("pip install pytesseract")
                    elif list_option == "8":
                        os.system("pip install Theano")
                    elif list_option == "9":
                        os.system("pip install tensorflow")
                    elif list_option == "10":
                        os.system("pip install keras")
                    elif list_option == "11":
                        os.system("pip install seaborn")
                    elif list_option == "12":
                        os.system("pip install scikit-learn")
                    elif list_option == "13":
                        os.system("pip install plotly")
                    elif list_option == "14":
                        os.system("pip install moviepy")
                    elif list_option == "15":
                        os.system("pip install scikit-video")
                    elif list_option == "16":
                        os.system("pip install vidgear")
                    elif list_option == "17":
                        os.system("pip install mahotas")
                    elif list_option == "18":
                        os.system("pip install Pillow")
                    elif list_option == "19":
                        os.system("pip install SimpleITK")
                    elif list_option == "20":
                        os.system("pip install pgmagick")
                    elif list_option == "21":
                        os.system("pip install SimpleCV")
                    elif list_option == "22":
                        os.system("pip install psutil")
                    elif list_option == "23":
                        os.system("pip install ctypes")
                    elif list_option == "24":
                        os.system("pip install codecs")
                    elif list_option == "25":
                        os.system("pip install paramiko")
                    elif list_option == "26":
                        os.system("pip install logging")
                    elif list_option == "27":
                        os.system("pip install salt")
                    elif list_option == "28":
                        os.system("pip install ansible")
                    elif list_option == "29":
                        os.system("pip install fabric")
                    elif list_option == "30":
                        os.system("pip install pywin32")
                    elif list_option == "31":
                        os.system("pip install selenium")
                    elif list_option == "32":
                        os.system("pip install beautifulsoup4")
                    elif list_option == "33":
                        os.system("pip install PyAutoGUI")
                    elif list_option == "34":
                        os.system("pip install pywinauto")
                    elif list_option == "35":
                        os.system("pip install requests")
                    elif list_option == "36":
                        os.system("pip install watchdog")
                    elif list_option == "37":
                        os.system("pip install python-csv")
                    elif list_option == "38":
                        os.system("pip install spliter")
                    elif list_option == "39":
                        os.system("pip install pytest")
                    elif list_option == "40":
                        os.system("pip install discord")
                    elif list_option == "41":
                        os.system("pip install nextcord")
                    elif list_option == "42":
                        os.system("pip install instagrapi")
                    elif list_option == "43":
                        os.system("pip install git+https://git@github.com/ping/instagram_private_api.git@1.6.0")
                    elif list_option == "44":
                        os.system("pip install telegram")
                    elif list_option == "45":
                        print(Colors.fgBlue + "[!] Going back ...")
                        python_libs()
                    elif list_option == "46":
                        print(Colors.fgRed + "[!] Exiting ...")
                        exit(0)
                    else:
                        print(Colors.fgRed + "[!] Invalid command , reloading")
                        lst()

                lst()

            if library_categories == "2":
                lib_name = input(Colors.fgWhite + "[*]" + Colors.fgCyan + " Enter name of library > ")
                os.system(f"pip install {lib_name}")

            elif library_categories == "3":
                print(Colors.fgBlue + "[!] Going back ...")
                menu()

            elif library_categories == "4":
                print(Colors.fgRed + "[!] Exiting ...")
                exit(0)
            else:
                print(Colors.fgRed + "[!] Invalid command , reloading")
                python_libs()

        python_libs()

    elif choice == "2":
        def categ_function():
            os.system("clear")
            print(Colors.fgBlue + """

      ,---.   ,--.--------.   _,.---._       _,.---._               
    .--.'  \ /==/,  -   , -\,-.' , -  `.   ,-.' , -  `.    _.-.     
    \==\-/\  \==\.-.  - ,-./==/_,  ,  - \ /==/_,  ,  - \ .-,.'|     
    /==/-|_\ |`--`\==\- \ |==|   .=.     |==|   .=.     |==|, |     
    \==\,   - \    \==\_ \|==|_ : ;=:  - |==|_ : ;=:  - |==|- |     
    /==/ -   ,|    |==|- ||==| , '='     |==| , '='     |==|, |     
    /==/-  /\ - \   |==|, | \==\ -    ,_ / \==\ -    ,_ /|==|- `-._  
    \==\ _.\=\.-'   /==/ -/  '.='. -   .'   '.='. -   .' /==/ - , ,/ 
    `--`           `--`--`    `--`--''       `--`--''   `--`-----'  
            """)

            print(Colors.fgCyan + """
        ====================================================
        ***************** All Categories *******************

        1) Information Gathering        10) Office
        2) Vulnerability Analysis       11) Customization
        3) Bluetooth Attacks            12) IDE's
        4) Web Applications             13) Browsers
        5) Sniffing & Spoofing          14) OSINT
        6) Exploitation Tools           15) Music
        7) Forensics Tools              16) Editing
        8) Phishing Tools               17) Wifi attacks
        9) Reverse Engineering          18) Crypto
                                        19) Cloud
                                        20) Exit
                                         
        f) Go to fist menu
        =======================================================
    """)

            category = input(Colors.fgWhite + "[*]" + Colors.fgCyan + " Choose a category > ")
            if category == "1":
                def information():
                    print(Colors.fgYellow + """
    =====================================
    [ Information Gathering ]

    1) Maltego Teeth    7) TheHarvester
    2) Burp Suite       8) Go back            
    3) Dnsrecon         9) Exit
    4) Parsero      
    5) Reconng         
    6) Fierce

    ======================================
        """)
                    ig = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgCyan + "] Information Gathering > ")
                    if ig == "1":
                        os.system("apt-get install maltego-teeth -yy ")
                        information()
                    elif ig == "2":
                        os.chdir("web")
                        os.system("bash burpsuite.sh")
                        information()
                    elif ig == "3":
                        os.chdir("information")
                        os.system("bash dnsrecon.sh")
                        information()
                    elif ig == "4":
                        os.chdir("information")
                        os.system("bash parsero.sh")
                        information()
                    elif ig == "5":
                        os.chdir("information")
                        os.system("bash reconng.sh")
                        information()
                    elif ig == "6":
                        os.chdir("information")
                        os.system("bash fierce.sh")
                        information()
                    elif ig == "7":
                        os.chdir("information")
                        os.system("bash harvester.sh")
                        information()
                    elif ig == "8":
                        print(Colors.fgBlue + "[!] Going back ...")
                        categ_function()
                    elif ig == "9":
                        print(Colors.fgRed + "[!] Exiting ...")
                        exit(0)
                    else:
                        print(Colors.fgRed + "[!] Invalid command , reloading")
                        information()

                information()

            elif category == "2":
                def vulnerability():
                    print(Colors.fgYellow + """
    ===========================
    [ Vulnerability Analysis ]

    1) BBQSQL              
    2) Nmap            
    3) Nikto                
    4) Sqlmap                  
    5) Burp Suite                                     
    6) Go back          
    7) Exit                                                           

    ===========================
        """)

                    va = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgBlue + "] Vulnerability analysis >")

                    if va == "2":
                        os.chdir("vuln")
                        os.system("bash bbqsql.sh")
                        vulnerability()
                    elif va == "3":
                        os.system("apt-get install nmap -yy")
                        vulnerability()
                    elif va == "8":
                        os.system("apt-get install sqlmap -yy")
                        vulnerability()
                    elif va == "13":
                        os.chdir("vuln")
                        os.system("bash nikto.sh")
                        vulnerability()
                    elif va == "14":
                        os.chdir("vuln")
                        os.system("bash burpsuite.sh")
                        vulnerability()
                    elif va == "15":
                        os.system("apt-get install sqlmap -yy")
                        print(Colors.fgBlue + "[!] Done ! ")
                        vulnerability()
                    elif va == "16":
                        print(Colors.fgBlue + "[!] Going back ...")
                        categ_function()
                    elif va == "17":
                        print(Colors.fgRed + "[!] Exiting ...")
                        exit(0)
                    else:
                        print(Colors.fgRed + "[!] Invalid command , reloading ")
                        vulnerability()

                vulnerability()

            elif category == "3":
                def wireless():
                    print(Colors.fgYellow + """

    ==============================================
    [ Bluetooth Attacks ]

    1) Bettercap
    2) Chkconfig
    3) Bluez
    4) sdptool
    5) Go back
    6) Exit

    0) Install all Wireless Attacks tools
    =================================================
        """)

                    wa = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgBlue + "] Bluetooth attacks >")

                    if wa == "1":
                        os.system("apt-get install bettercap -yy ")
                        wireless()
                    elif wa == "2":
                        os.system("apt-get install chkconfig -yy")
                        wireless()
                    elif wa == "3":
                        os.system("snap install bluez")
                        wireless()
                    elif wa == "4":
                        print(Colors.fgBlue + "[!] Spdtool is already installed to every linux system by default")
                        wireless()
                    elif wa == "5":
                        print(Colors.fgBlue + "[!] Going back ....")
                        categ_function()
                    elif wa == "6":
                        print(Colors.fgRed + "[!] Exiting ..")
                        exit(0)
                    elif wa == "0":
                        print(Colors.fgBlue + "[!] Installing all tools ")
                        os.system("apt-get install bettercap -yy && apt-get install chkconfig -yy && snap install bluez")
                        print(Colors.fgBlue + "[!!] Installed all tools .......")
                    else:
                        print(Colors.fgRed + "[!] Invalid command , reloading")
                        wireless()

                wireless()

            elif category == "4":
                def web():
                    print(Colors.fgYellow + """
    ================================================
    [ Web Applications ]

    1) Simple Http-server        15) phpsploit
    2) Sqlmap                    16) Xaamp 
    3) Apache2                   17) XAttacker
    4) Burp Suite                18) Go back
    5) Owasp                     19) Exit
    6) Dns-spoof                 
    7) bEEF                
    8) W3af                    
    9) Wpscan                       
    10) Websploit
    11) Commix
    12) Nikto  
    13) Recon-ng 
    14) Parsero 

    ===============================================
        """)

                    wapp = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgCyan + "] web applications > ")

                    if wapp == "1":
                        print(Colors.fgBlue + "[!] To run Simple Http server simple execute : python -m SimpleHTTPServer")
                        web()
                    elif wapp == "2":
                        os.system("apt-get install sqlmap -yy")
                        web()
                    elif wapp == "3":
                        os.system("apt-get install apache2 -yy")
                        web()
                    elif wapp == "4":
                        os.chdir("web")
                        os.system("bash burpsuite.sh")
                        web()
                    elif wapp == "5":
                        os.chdir("web")
                        os.system("bash owasp.sh")
                        web()
                    elif wapp == "6":
                        os.system("apt-get install dsniff -yy")
                        web()
                    elif wapp == "7":
                        os.chdir("web")
                        os.system("bash beef.sh")
                        web()
                    elif wapp == "8":
                        os.system("apt-get install -y w3af -yy")
                        web()
                    elif wapp == "9":
                        os.chdir("web")
                        os.system("bash wps.sh")
                        web()
                    elif wapp == "10":
                        os.chdir("vulnerability")
                        os.system("bash commix.sh")
                        web()
                    elif wapp == "11":
                        os.chdir("vuln")
                        os.system("bash nikto.sh")
                        web()
                    elif wapp == "12":
                        os.chdir("information")
                        os.system("bash reconng.sh")
                        web()
                    elif wapp == "13":
                        os.chdir("information")
                        os.system("bash parsero.sh")
                        web()
                    elif wapp == "14":
                        os.chdir("web")
                        os.system("bash php.sh")
                        web()
                    elif wapp == "15":
                        os.chdir("web")
                        os.system("bash xaamp.sh")
                        web()
                    elif wapp == "16":
                        print(Colors.fgBlue + "[!] Going back...")
                        categ_function()
                    elif wapp == "17":
                        print(Colors.fgRed + "[!] Exiting ...")
                        exit(0)
                    else:
                        print(Colors.fgRed + "[!] Invalid command , reloading")
                        web()

                web()

            elif category == "5":
                def sniffing():
                    print(Colors.fgYellow + """

    =========================================
        [ Sniffing & Spoofing ]

    1) Burp Suite     14) evilgrade 
    2) Wireshark      15) Go back
    3) Bettercap      16) Exit 
    4) etherape
    5) hamster
    6) mitmproxy
    7) macchanger
    8) netsniff-ng
    9) wifi-honey
    10) dnsspoof
    11) exinject 
    12) Driftnet
    13) darkstat
    
    ================================================
        """)

                    sst = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgCyan + "] sniffing & spoofing > ")

                    if sst == "1":
                        os.chdir("sniffing")
                        os.system("bash burp.sh")
                        sniffing()
                    elif sst == "2":
                        os.system("apt-get install wireshark -yy")
                        sniffing()
                    elif sst == "3":
                        os.system("apt-get install bettercap -yy")
                        sniffing()
                    elif sst == "4":
                        os.system("apt-get install etherape -yy")
                        sniffing()
                    elif sst == "5":
                        os.system("apt-get install hamster-sidejack -yy")
                        sniffing()
                    elif sst == "6":
                        os.system("python3 -m pip install --user pipx")
                        os.system("pipx install mitmproxy")
                        sniffing()
                    elif sst == "7":
                        os.system("apt-get install macchanger -yy")
                        sniffing()
                    elif sst == "8":
                        os.system("apt-get install netsniff-ng -yy")
                        sniffing()
                    elif sst == "9":
                        os.system("apt-get install wifi-honey -yy")
                        sniffing()
                    elif sst == "10":
                        os.system("apt-get install dnsniff")
                        sniffing()
                    elif sst == "11":
                        os.system("apt-get install hexinject -yy")
                        sniffing()
                    elif sst == "12":
                        os.system("apt-get install driftnet -yy")
                        sniffing()
                    elif sst == "13":
                        os.system("apt-get install libpcap-dev -yy")
                        os.system("apt-get install darkstat -yy")
                        sniffing()
                    elif sst == "14":
                        os.chdir("sniffing")
                        os.system("bash evilgrade.sh")
                        sniffing()
                    elif sst == "15":
                        print(Colors.fgBlue + "[!] Going back ...")
                        categ_function()
                    elif sst == "16":
                        print(Colors.fgRed + "[!] Exiting ..")
                        exit(0)
                    else:
                        print(Colors.fgRed + "[!] Invalid command , reloading")
                        sniffing()

                sniffing()

            elif category == "6":
                def exploit():
                    print(Colors.fgYellow + """
    ====================================
    [ Exploitation Tools ]

    1) Metasploit & Armitage
    4) BeEF
    5) Burp Suite
    7) Maltego Teeth
    8) SET
    9) sqlmap
    11) Evil-Droid
    12) Go back 
    13) Exit

    ====================================
        """)
                    et = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgCyan + "] Exploitation > ")

                    if et == "1":
                        os.chdir("exploitation")
                        os.system("bash msfarmitage.sh")
                        exploit()
                    elif et == "4":
                        os.chdir("exploitation")
                        os.system("bash beef.sh")
                        exploit()
                    elif et == "5":
                        os.chdir("web")
                        os.system("bash burpsuite.sh")
                        exploit()
                    elif et == "6":
                        os.system("apt-get install -y aircrack-ng -yy")
                        exploit()
                    elif et == "7":
                        os.system("apt-get install maltego-teeth -yy ")
                        exploit()
                    elif et == "8":
                        os.chdir("exploitation")
                        os.system("bash set.sh")
                        exploit()
                    elif et == "9":
                        os.system("apt-get install sqlmap -yy")
                        exploit()
                    elif et == "11":
                        os.chdir("exploitation")
                        os.system("bash evildroid.sh")
                        exploit()
                    elif et == "12":
                        print(Colors.fgBlue + "[!] Going back ...")
                        categ_function()
                    elif et == "13":
                        print(Colors.fgRed + "[!] Exiting....")
                        exit(0)
                    else:
                        print(Colors.fgRed + "[!] Invalid command , reloading")
                        exploit()

                exploit()

            elif category == "7":
                def forensics():
                    print(Colors.fgYellow + """
    ======================================================
    [ Forensics Tools ]

    1) BinWalk               11) John The ripper
    2) bulk-extractor        12) xplico
    3) Capstone              13) zsteg
    4) diStorm3              14) hindsight
    5) Pdf-parser            15) Mac-Locations scraper
    6) volatility            16) Go back
    7) HashDeep              17) Exit
    8) chkrootkit
    9) Sleuth Forensics kit 
    10) Caine OS 

    ======================================================
        """)

                    ft = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgCyan + "] forensics >  ")

                    if ft == "1":
                        os.chdir("forensics")
                        os.system("bash binwalk.sh")
                        forensics()
                    elif ft == "2":
                        os.chdir("forensics")
                        os.system("bash bulk.sh")
                        forensics()
                    elif ft == "3":
                        os.chdir("forensics")
                        os.system("bash capstone.sh")
                        forensics()
                    elif ft == "4":
                        os.system("apt-get install python-distorm3 -yy")
                        forensics()
                    elif ft == "5":
                        os.chdir("forensics")
                        os.system("bash pdffparser.sh")
                        forensics()
                    elif ft == "6":
                        os.chdir("forensics")
                        os.system("bash volatolity.sh")
                        forensics()
                    elif ft == "7":
                        os.chdir("forensics")
                        os.system("bash hashdeep.sh")
                        forensics()
                    elif ft == "8":
                        os.chdir("forensics")
                        os.system("bash chkrootkit.sh")
                        forensics()
                    elif ft == "9":
                        os.chdir("forensics")
                        os.system("bash sleuth.sh")
                        forensics()
                    elif ft == "10":
                        os.chdir("forensics")
                        os.system("bash caine.sh")
                        forensics()
                    elif ft == "11":
                        os.system("snap install john-the-ripper")
                        forensics()
                    elif ft == "12":
                        os.chdir("information")
                        os.system("bash xplico.sh")
                        forensics()
                    elif ft == "13":
                        os.system("gem install zsteg")
                        forensics()
                    elif ft == "14":
                        os.chdir("forensics")
                        os.system("bash hindsight.sh")
                        forensics()
                    elif ft == "15":
                        os.chdir("forensics")
                        os.system("bash maclocsraper.sh")
                        forensics()
                    elif ft == "16":
                        print(Colors.fgBlue + "[!] Going back ...")
                        categ_function()
                    elif ft == "17":
                        print(Colors.fgRed + "[!] Exiting....")
                        exit(0)
                    else:
                        print(Colors.fgRed + "[!] Invalid command , reloading")
                        forensics()

                forensics()

            elif category == "8":
                def phish():
                    print(Colors.fgBlue + """
    ==========================================
    [ Phishing tools ]

    1) SocialPhish   7) Zphisher
    2) Nexphisher    8) King-phisher
    3) LordPhish     9) Maskphish
    4) HiddenEye     10) Tools-phishing
    5) AdvPhishing   11) GoPhish
    6) wifiphisher   12) Go back 
                     13) Exit

    ==========================================
        """)

                    phi = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgCyan + "] Phishing tools > ")

                    if phi == "1":
                        os.chdir("phish")
                        os.system("bash socialphish.sh")
                        phish()
                    elif phi == "2":
                        os.chdir("phish")
                        os.system("bash nex.sh")
                        phish()
                    elif phi == "3":
                        os.chdir("phish")
                        os.system("bash lord.sh")
                        phish()
                    elif phi == "4":
                        os.chdir("phish")
                        os.system("bash hidden.sh")
                        phish()
                    elif phi == "5":
                        os.chdir("phish")
                        os.system("bash adv.sh")
                        phish()
                    elif phi == "6":
                        os.chdir("phish")
                        os.system("bash wifiphisher.sh")
                        phish()
                    elif phi == "7":
                        os.chdir("phish")
                        os.system("bash zphisher.sh")
                        phish()
                    elif phi == "8":
                        os.chdir("phish")
                        os.system("bash king.sh")
                        phish()
                    elif phi == "9":
                        os.chdir("phish")
                        os.system("bash mask.sh")
                        phish()
                    elif phi == "10":
                        os.chdir("phish")
                        os.system("bash toolsphish.sh")
                        phish()
                    elif phi == "11":
                        os.chdir("phish")
                        os.system("bash gogh.sh")
                        phish()
                    elif phi == "12":
                        print(Colors.fgBlue + "[!] Going back")
                        categ_function()
                    elif phi == "13":
                        print(Colors.fgRed + "[!] Exiting..")
                        exit(0)
                    else:
                        print(Colors.fgRed + "[!] Invalid command , reloading")
                        phish()

                phish()

            elif category == "9":
                def reverse():
                    print(Colors.fgYellow + """
    =====================================
    [ Reverse Engineering ]
    
    1) Ghirda           9) OllyDbg
    2) apktool          10) smali
    3) dex2jar          11) Valgrind
    4) diStorm3         12) Go back
    5) edb-debugger     13) Exit
    6) jad	
    7) javasnoop
    8) JD-GUI

    ====================================

        """)
                    rev = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgCyan + "] reverse engineering > ")

                    if rev == "1":
                        os.chdir("reverse")
                        os.system("bash ghirda.sh")
                        reverse()
                    if rev == "2":
                        os.system("snap install apktool")
                        reverse()
                    elif rev == "3":
                        os.system("apt-get install dex2jar -yy")
                        reverse()
                    elif rev == "4":
                        os.system("apt-get install python-diStorm3 -yy")
                        reverse()
                    elif rev == "5":
                        os.system("apt-get install edb-debugger -yy")
                        reverse()
                    elif rev == "6":
                        os.system("apt-get install jad -yy")
                        reverse()
                    elif rev == "7":
                        os.system("apt-get install javasnoop -yy")
                        reverse()
                    elif rev == "8":
                        os.system("apt-get install JD -yy")
                        reverse()
                    elif rev == "9":
                        os.system("apt-get install OllyDbg -yy")
                        reverse()
                    elif rev == "10":
                        os.system("apt-get install smali -yy")
                        reverse()
                    elif rev == "11":
                        os.system("apt-get install Valgrind -yy")
                        reverse()
                    elif rev == "12":
                        print(Colors.fgBlue + "[!] Going back... ")
                        categ_function()
                    elif rev == "13":
                        print(Colors.fgRed + "[!] Exiting ...")
                        exit(0)
                    else:
                        print(Colors.fgRed + "[!] Invalid command , reloading")
                        reverse()

                reverse()

            elif category == "10":
                def office_software():
                    print(Colors.fgYellow + """
    ====================================================

    [ Office software ]

    1) LibreOffice            5) Scite        
    2) Calculator             6) Geany              
    3) Evince Pdf reader      7) Go back             
    4) Okular pdf reader      8) Exit

    ======================================================
        """)

                    office = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgCyan + "] office > ")

                    if office == "1":
                        print(Colors.fgBlue + "[!]Installing LibreOffice ")
                        os.system("apt-get install libreoffice -yy")
                        office_software()
                    elif office == "2":
                        print(Colors.fgBlue + "[!] Installing Xcalculator")
                        os.system("apt-get install -y xsmc-calc")
                        office_software()
                    elif office == "3":
                        print(Colors.fgBlue + "[!] Installing Evince Pdf Reader ")
                        os.system("apt-get install evince -yy")
                        office_software()
                    elif office == "4":
                        print(Colors.fgBlue + "[!] Installing Okular pdf reader ")
                        os.system("apt-get install okular -yy")
                        office_software()
                    elif office == "5":
                        print(Colors.fgBlue + "[!] Installing Scite text editor ")
                        os.system("apt-get install scite -yy")
                        office_software()
                    elif office == "6":
                        print(Colors.fgBlue + "[!] Installing Geany ")
                        os.system("apt-get install geany -yy")
                        office_software()
                    elif office == "7":
                        print(Colors.fgBlue + "[!] Going back ...")
                        categ_function()
                    elif office == "8":
                        print(Colors.fgRed + "[!] Exiting .... ")
                        exit(0)
                    else:
                        print(Colors.fgRed + "[!] Invalid command , reloading")
                        office_software()

                office_software()

            elif category == "11":
                def customization():
                    print(Colors.fgYellow + """
    ==============================================
    [ Customization ]

    1) Tweaks (For Gnome)     4) Fondo
    2) Gogh                   5) Go to main menu
    3) Komorebi               6) Exit
       
    ===============================================
        """)

                    custom = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgCyan + "] customization >  ")

                    if custom == "1":
                        print(Colors.fgBlue + "[!] Installing Tweaks tool (Supported for gnome terminal only)")
                        os.system("apt-get install gnome-tweak-tool -yy")
                        os.system("apt-get update -yy")
                        customization()
                    elif custom == "2":
                        print(Colors.fgBlue + "[!] Installing Gogh")
                        os.chdir("customization")
                        os.system("bash go.sh")
                        customization()
                    elif custom == "3":
                        os.chdir("customization")
                        os.system("bash komorebi.sh")
                        customization()
                    elif custom == "4":
                        os.chdir("customization")
                        os.system("bash fondo.sh")
                        customization()
                    elif custom == "5":
                        print(Colors.fgBlue + "[!] Going back .. ")
                        categ_function()
                    elif custom == "6":
                        print(Colors.fgRed + "[!] Exiting .. ")
                        exit(0)
                    else:
                        print(Colors.fgRed + "[!] Invalid command , reloading")
                        customization()

                customization()

            elif category == "12":
                def ides():
                    print(Colors.fgYellow + """
        ===============================================
        [ IDE's for coding ]

        1) Vscode         6) Webstorm
        2) Pycharm        7) IntelliJ IDEA
        3) Atom           8) NetBeans
        4) Geany          9) Android studio 
        5) Sublime Text   10) Go back
                          11) Exit

        ================================================
        """)

                    ide = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgCyan + "] Choose an IDE  >  ")

                    if ide == "1":
                        os.chdir("ides")
                        os.system("bash code.sh")
                        ides()
                    elif ide == "2":
                        print(Colors.fgBlue + "Installing Pycharm community edition from snap ")
                        os.system("sudo snap install pycharm-community --classic")
                        ides()
                    elif ide == "3":
                        print(Colors.fgBlue + "[!] Installing Atom with snap !")
                        os.system("sudo snap install atom --classic")
                        ides()
                    elif ide == "4":
                        print(Colors.fgBlue + "[!] Installing Geany from snap !")
                        os.system("sudo apt-get update -yy ")
                        os.system("sudo apt-get install geany -yy ")
                        ides()
                    elif ide == "5":
                        os.chdir("ides")
                        os.system("bash sublime.sh")
                        ides()
                    elif ide == "6":
                        os.chdir("ides")
                        os.system("bash web.sh")
                        ides()
                    elif ide == "7":
                        print(Colors.fgBlue + "[!] Installing Intellij IDEA !")
                        os.system("sudo apt-get install snapd -yy ")
                        os.system("sudo snap install intellij-idea-community --classic")
                        ides()
                    elif ide == "8":
                        print(Colors.fgBlue + "[!] Installing NetBeans ! ")
                        os.system("sudo apt install default-jdk -yy")
                        os.system("sudo snap install netbeans --classic")
                        ides()
                    elif ide == "9":
                        print(Colors.fgBlue + "[!] Installing Android studio ! ")
                        os.system("sudo apt-get install openjdk-11-jdk -yy")
                        os.system("sudo apt-get update -yy")
                        os.system("snap install android-studio")
                        ides()
                    elif ide == "10":
                        print(Colors.fgBlue + "[!] Going back..")
                        categ_function()
                    elif ide == "11":
                        print(Colors.fgRed + "[!] Exiting...")
                        exit(0)
                    else:
                        print(Colors.fgRed + "[!] Invalid command , reloading")
                        ides()

                ides()

            elif category == "13":
                def browsers():
                    print(Colors.fgYellow + """
    ====================================  
    [Browsers] 
                
    1) Firefox  4) Brave
    2) Chrome   5) Go back
    3) Tor      6) Exit    
    
    =====================================                                       
        """)

                    brow = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgCyan + "] browsers > ")

                    if brow == "1":
                        print(Colors.fgBlue + "[!] Installing Firefox !")
                        os.system("apt-get install firefox-esr -yy ")
                        browsers()
                    elif brow == "2":
                        os.chdir("browsers")
                        os.system("bash google.sh")
                        browsers()
                    elif brow == "3":
                        print(Colors.fgBlue + "[!] Installing Tor!")
                        os.system("sudo apt update -yy")
                        os.system("sudo apt install torbrowser-launcher -yy ")
                        browsers()
                    elif brow == "4":
                        os.chdir("browsers")
                        os.system("bash brave.sh")
                        browsers()
                    elif brow == "5":
                        print(Colors.fgBlue + "[!] Going back...")
                        categ_function()
                    elif brow == "6":
                        print(Colors.fgRed + "[!] Exiting ...")
                        exit(0)
                    else:
                        print(Colors.fgRed + "[!] Invalid command , reloading")
                        browsers()

                browsers()

            elif category == "14":
                def osint_tools_function():
                    print(Colors.fgYellow + """
    =========================================
    [OSINT tools]

    1) Osinted           9) Go back
    2) Osintgram         10) Exit
    3) SatIntel              
    4) Osint Framework   
    5) Metagoofil              
    6) Sherlock              
    7) Spider Foot
    8) Facebook-Scraper
    

    =========================================
        """)

                    osint_tools = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgCyan + "] osint tools >")

                    if osint_tools == "1":
                        os.chdir("osint")
                        os.system("osinted.sh")
                        osint_tools_function()
                    elif osint_tools == "2":
                        os.chdir("osint")
                        os.system("bash osintgram.sh")
                        osint_tools_function()
                    elif osint_tools == "3":
                        os.chdir("osint")
                        os.system("bash satintel.sh")
                        osint_tools_function()
                    elif osint_tools == "4":
                        print(Colors.fgBlue + "Visit: " + Colors.fgMagenta + "https://osintframework.com")
                        time.sleep(3)
                        osint_tools_function()
                    elif osint_tools == "5":
                        os.system("sudo apt-get install metagoofil -yy")
                        osint_tools_function()
                    elif osint_tools == "6":
                        os.chdir("osint")
                        os.system("bash sherlock.sh")
                        osint_tools_function()
                    elif osint_tools == "7":
                        os.chdir("osint")
                        os.system("bash spiderfoot.sh")
                        osint_tools_function()
                    elif osint_tools == "8":
                        os.chdir("osint")
                        os.system("bash face.sh")
                        osint_tools_function()
                    elif osint_tools == "9":
                        print(Colors.fgBlue + "[!] Going back  ..")
                        categ_function()
                    elif osint_tools == "10":
                        print(Colors.fgRed + "[!] Exiting...")
                        exit(0)
                    else:
                        print(Colors.fgRed + "[!] Invalid choice , reloading .")
                        osint_tools_function()

                osint_tools_function()

            elif category == "15":
                def music_function():
                    print(Colors.fgYellow + """
    =========================
            [Music]

    1) Spotify    5) Go back 
    2) Rhythmbox  6) Exit
    3) Vlc
    4) Clementine 

    =========================
        """)

                    music_software = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgCyan + "] music >")

                    if music_software == "1":
                        os.system("snap install spotify")
                        music_function()
                    elif music_software == "2":
                        os.chdir("music")
                        os.system("rhythmbox.sh")
                        music_function()
                    elif music_software == "3":
                        os.system("sudo snap install vlc")
                        music_function()
                    elif music_software == "4":
                        os.chdir("music")
                        os.system("bash clementine.sh")
                        music_function()
                    elif music_software == "5":
                        print(Colors.fgBlue + "[!] Going back")
                        categ_function()
                    elif music_software == "6":
                        print(Colors.fgRed + "[!] Exiting..")
                        exit(0)
                    else:
                        print(Colors.fgRed + "[!] Invalid command, reloading")
                        music_function()

                music_function()

            elif category == "16":
                def editing_function():
                    print(Colors.fgYellow + """
    ==========================
    [Editing/Recording]

    1) Kdenlive 4) OBS Studio
    2) GNU      5) Go back
    3) Kazam    6) Exit

    ==========================
        """)
                    editing_software = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgCyan + "] editing >")

                    if editing_software == "1":
                        os.system("snap install kdenlive")
                        editing_function()
                    elif editing_software == "2":
                        os.system("sudo snap install gimp")
                        editing_function()
                    elif editing_software == "3":
                        os.system("apt-get install kazam -yy")
                        editing_function()
                    elif editing_software == "4":
                        os.system("apt-get install obs-studio -yy")
                        editing_function()
                    elif editing_software == "5":
                        print(Colors.fgBlue + "[!] Going back ...")
                        categ_function()
                    elif editing_software == "6":
                        print(Colors.fgRed + "[!] Exiting..")
                        exit(0)
                    else:
                        print(Colors.fgRed + "[!] Invalid command ,reloading")
                        editing_function()

                editing_function()

            elif category == "17":
                def wifi_attacks():
                    print(Colors.fgYellow + """
    =========================================
    [ Wifi Attacks ]

    1) Aircrack-ng             8) Wifitap
    2) Pixiewps                9) Wifi Honey  
    3) Wireshark               10) Evil limiter 
    4) Wifite                  11) wifi-hacking  
    5) Wash                    12) Fluxion
    6) Crunch                  13) Go back
    7) mkd3                    14) Exit

    =========================================
        """)

                    wif = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgCyan + "] wifi tools >")

                    if wif == "1":
                        os.chdir("wifi")
                        os.system("bash air.sh")
                        wifi_attacks()
                    elif wif == "2":
                        os.chdir("wifi")
                        os.system("bash pixie.sh")
                        wifi_attacks()
                    elif wif == "3":
                        os.system("apt-get install wireshark -yy")
                        wifi_attacks()
                    elif wif == "4":
                        os.chdir("wifi")
                        os.system("bash wifite.sh")
                        wifi_attacks()
                    elif wif == "5":
                        os.system("apt-get install wash -yy ")
                        wifi_attacks()
                    elif wif == "6":
                        os.system("apt-get install crunch")
                        wifi_attacks()
                    elif wif == "7":
                        os.system("apt-get install mdk3 -yy")
                        wifi_attacks()
                    elif wif == "8":
                        os.system("apt-get install wifitap -yy ")
                        wifi_attacks()
                    elif wif == "9":
                        os.chdir("wifi")
                        os.system("bash wifihoney.sh")
                        wifi_attacks()
                    elif wif == "10":
                        os.chdir("wifi")
                        os.system("bash evil.sh")
                        wifi_attacks()
                    elif wif == "11":
                        os.chdir("wifi")
                        os.system("bash wifih.sh")
                        wifi_attacks()
                    elif wif == "12":
                        os.chdir("wifi")
                        os.system("bash flux.sh")
                        wifi_attacks()
                    elif wif == "13":
                        print(Colors.fgBlue + "[!] Going back ...")
                        categ_function()
                    elif wif == "14":
                        exit(Colors.fgRed + "[!] Exiting... ")
                    else:
                        print(Colors.fgRed + "[!] Invalid command , reloading")
                        wifi_attacks()

                wifi_attacks()

            elif category == "18":
                def crypto():
                    print(Colors.fgYellow + """
    ===============================
              [Crypto]
              
    1) Exodus         5) Exit
    2) Electrum 
    3) Coinomi
    4) Go back 

    ================================
                    
        """)
                    c = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgCyan + "] crypto > ")

                    if c == "1":
                        os.chdir("crypto")
                        os.system("bash .sh")
                        crypto()
                    elif c == "2":
                        os.chdir("crypto")
                        os.system("bash .sh")
                        crypto()
                    elif c == "3":
                        os.chdir("crypto")
                        os.system("bash .sh")
                        crypto()
                    elif c == "4":
                        print(Colors.fgBlue + "[!] Going back ...")
                        categ_function()
                    elif c == "5":
                        print(Colors.fgRed + "[!] Exiting ..")
                        exit(0)
                    else:
                        print(Colors.fgRed + "[!] Invalid command , reloading")
                        crypto()

                crypto()

            elif category == "19":
                def cloud():
                    print(Colors.fgYellow + """
    ============================
            [ Cloud ]

    1) Mega.nz     5) Go back
    2) Nextcloud   6) Exit
    3) Seafile 
    4) Dropbox   

    ===========================
                        """)

                    cloud_option = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgCyan + "] Cloud > ")

                    if cloud_option == "1":
                        os.chdir("cloud")
                        os.system("bash mega.sh")

                    elif cloud_option == "2":
                        os.chdir("cloud")
                        os.system("bash nextcloud.sh")

                    elif cloud_option == "3":
                        os.chdir("cloud")
                        os.system("bash seafile.sh")

                    elif cloud_option == "4":
                        os.chdir("cloud")
                        os.system("bash dropbox.sh")

                    elif cloud_option == "5":
                        print(Colors.fgBlue + "[!] Going back ...")
                        categ_function()
                    elif cloud_option == "6":
                        exit(Colors.fgRed + "[!] Exiting ..")
                    else:
                        print(Colors.fgRed + "[!] Invalid command , reloading")
                        cloud()

                cloud()

            elif category == "20":
                print(Colors.fgRed + "[!] Exiting ...")
                exit(0)
            elif category == "f":
                print(Colors.fgBlue + "[!] Going back ...")
                time.sleep(2)
                os.system("clear")
                menu()
            else:
                print(Colors.fgRed + "[!] Invalid choice , reloading ")
                time.sleep(3)
                categ_function()

        categ_function()

    elif choice == "3":
        print(Colors.fgBlue + "[!] Updating & upgrading system")
        os.system("apt-get update -yy && apt-get full-upgrade -yy && apt-get autoremove -yy")
        menu()

    elif choice == "4":
        def second_menu():
            print(Colors.fgCyan + """
    ==============================================================
                [ Useful/Popular Apps/Tools ]
    
    1) Chrome        11) Obs Studio       21) Aircrack-ng
    2) Brave         12) Kdenlive         22) Wireshark
    3) Tor           13) Kazam            23) Fluxion
    4) Pycharm       14) Spotify          24) PixieWps
    5) Geany         15) VLC              25) Mega.nz 
    6) Vscode        16) Rhythmbox        26) Gnome tweaks
    7) Virtualbox    17) Osintgram        27) Hydra
    8) Wine          18) Firefox          28) Maltego
    9) Tweaks        19) Gnu Mac changer  29) Hashcat 
    10) Gogh         20) Ghirda           30) Airgeddon 
                                          31) Mullvad Vpn
                                          32) Go back 
                                          33) Exit 
                                             
    =============================================================
    """)
            sec_option = input(Colors.fgBlue + "[" + Colors.fgWhite + "*" + Colors.fgCyan + "] >> ")

            if sec_option == "1":
                os.chdir("browsers")
                os.system("bash google.sh")
                second_menu()

            elif sec_option == "2":
                os.chdir("browsers")
                os.system("bash brave.sh")
                second_menu()

            elif sec_option == "3":
                os.system("sudo apt update -yy")
                os.system("sudo apt install torbrowser-launcher -yy ")
                second_menu()

            elif sec_option == "4":
                print(Colors.fgBlue + "Installing Pycharm community edition from snap ")
                os.system("sudo snap install pycharm-community --classic")
                second_menu()

            elif sec_option == "5":
                print(Colors.fgBlue + "[!] Installing Geany from snap !")
                os.system("sudo apt-get update -yy ")
                os.system("sudo apt-get install geany -yy ")
                second_menu()

            elif sec_option == "6":
                os.chdir("ides")
                os.system("bash code.sh")
                second_menu()

            elif sec_option == "7":
                os.system("apt-get install virtualbox -yy")
                os.system("apt-get install virtualbox-ext-pack -y")
                second_menu()

            elif sec_option == "8":
                os.system("dpkg --add-architecture i386 && apt-get update -yy && apt-get install wine32 -yy apt-get install wine64 -yy")
                second_menu()

            elif sec_option == "9":
                os.system("apt-get install gnome-tweaks -yy")
                second_menu()

            elif sec_option == "10":
                os.chdir("customization")
                os.system("bash go.sh")
                second_menu()

            elif sec_option == "11":
                os.system("apt-get install obs-studio -yy")
                second_menu()

            elif sec_option == "12":
                os.system("snap install kdenlive -yy")
                second_menu()

            elif sec_option == "13":
                os.system("apt-get install kazam -yy")
                second_menu()

            elif sec_option == "14":
                os.system("snap install spotify")
                second_menu()

            elif sec_option == "15":
                os.system("sudo snap install vlc")
                second_menu()

            elif sec_option == "16":
                os.chdir("music")
                os.system("bash rhythmbox.sh")
                second_menu()

            elif sec_option == "17":
                os.chdir("osint")
                os.system("bash osintgram.sh")
                second_menu()

            elif sec_option == "18":
                os.system("apt-get install firefox -yy")
                second_menu()

            elif sec_option == "19":
                os.system("apt-get install macchanger -yy")
                second_menu()

            elif sec_option == "20":
                os.chdir("reverse")
                os.system("bash ghirda.sh")
                second_menu()

            elif sec_option == "21":
                os.chdir("wifi")
                os.system("bash air.sh")
                second_menu()

            elif sec_option == "22":
                os.system("apt-get install wireshark -yy")
                second_menu()

            elif sec_option == "23":
                os.chdir("wifi")
                os.system("bash flux.sh")
                second_menu()

            elif sec_option == "24":
                os.system("apt-get install libssl-dev -yy")
                os.system("apt-get install libssl-dev")
                os.system("apt-get install pixiewps -yy")
                second_menu()

            elif sec_option == "25":
                os.chdir("cloud")
                os.system("bash mega.sh")
                second_menu()

            elif sec_option == "26":
                os.system("apt-get install gnome-tweaks -yy")
                second_menu()

            elif sec_option == "27":
                os.system("apt-get -y install build-essential")
                os.system("apt-get install hydra-gtk -yy ")
                second_menu()

            elif sec_option == "28":
                os.system("apt-get install maltego -yy ")
                second_menu()

            elif sec_option == "29":
                os.system("apt-get install hashcat -yy ")
                second_menu()

            elif sec_option == "30":
                os.chdir("wifi")
                os.system("bash air.sh")
                second_menu()

            elif sec_option == "31":
                print(Colors.fgBlue + "[!] Downloading & installing Mullvad Vpn")
                os.system("wget https://mullvad.net/en/download/app/deb/latest")
                os.system("dpkg -i MullvadVPN-2023.4_amd64.deb")
                second_menu()

            elif sec_option == "32":
                print(Colors.fgBlue + "[!] Going back .........")
                menu()

            elif sec_option == "33":
                exit(Colors.fgRed + "[!] Exiting ..")

            elif sec_option == "clear":
                os.system("clear")
                second_menu()
            else:
                print(Colors.fgRed + "[!] Invalid command , reloading")
                second_menu()

        second_menu()

    elif choice == "5":
        os.system("bash custom.sh")

    elif choice == "6":
        help_screen = Colors.fgGreen + """
    ==========================================
    ***************** Help *******************

    [!] To recommend tools that should be added 
    contact me on discord @punchmadecoder
    
    Type \'clear\' to clear the screen
    
    ==========================================

    """
        input(help_screen)
        os.system("clear")
        menu()

    elif choice == "7":
        print(Colors.fgRed + "[!] Exiting ..")
        exit(0)

    elif choice == "clear":
        os.system("clear")
        menu()

    else:
        print(Colors.fgRed + "[!] Invalid option ,reloading ")
        os.system("clear")
        menu()


menu()
