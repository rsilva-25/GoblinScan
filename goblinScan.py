import os

print("tookit for scanning websites and wifi networks\n")

def banner():
    print("\x1b[92m")
    print(r""" ███   ███  ████  █     ███ █   █  ████  ███   ███  █   █ 
█     █   █ █   █ █      █  ██  █ █     █     █   █ ██  █ 
█  ██ █   █ ████  █      █  █ █ █  ███  █     █████ █ █ █ 
█   █ █   █ █   █ █      █  █  ██     █ █     █   █ █  ██ 
 ███   ███  ████  █████ ███ █   █ ████   ███  █   █ █   █  """)

    print("\x1b[00m")

    print("\x1b[33m")
    print("\n Create by: rsilva25")
    print("\x1b[00m")

def menu():
    print("\n\x1b[33m[1]\x1b[00m Nmap Scan")
    print("\x1b[33m[2]\x1b[00m Gobuster Scan")
    print("\x1b[33m[9]\x1b[00m How it works?")
    print("\x1b[33m[0]\x1b[00m Exit")


def nmap_menu():
    print("<---- nmap Menu ---->")
    print("\x1b[33m[1]\x1b[00m Full Scan")
    print("\x1b[33m[2]\x1b[00m Fast Scan")
    print("\x1b[33m[3]\x1b[00m Port Scan")
    print("\x1b[33m[4]\x1b[00m OS and versions Scan")
    print("\x1b[33m[0]\x1b[00m Back")


def gobuster_menu():
    print("<---- gobuster ---->")
    print("\x1b[33m[1]\x1b[00m Small Scan")
    print("\x1b[33m[2]\x1b[00m Commun Scan")
    print("\x1b[33m[3]\x1b[00m Big Scan")
    print("\x1b[33m[0]\x1b[00m Back")


while True:
    banner()
    menu()
    opcao = input("\nSelect an option: ")

    match opcao:
        case "1":
            while True:
                nmap_menu()

                nmap_types = {
                    "1": "Fast Scan",
                    "2": "Full Scan",
                    "3": "Ports Scan",
                    "4": "OS & Versions Scan"
                }

                sub = input("\nSelect the scan type: ")
                print(f"-> {nmap_types.get(sub, 'Invalid Option')}")
                match sub:
                    case "1":
                        target = input("\x1b[33m IP/Domain: \x1b[00m")
                        os.system(f"nmap -sS -sV -sC -O -T2 --reason {target}")

                    case "2":
                        target = input("\x1b[33m IP/Domain: \x1b[00m")
                        os.system(f"nmap -sS -sV -O -T4 --reason {target}")

                    case "3":
                        target = input("\x1b[33m IP/Domain: \x1b[00m")
                        os.system(f"nmap -p- -sS -T4 --reason {target}")

                    case "4":
                        target = input("\x1b[33m IP/Domain: \x1b[00m")
                        os.system(f"nmap -sS -sV -O -T2 {target}")

                    case "0":
                        break

                    case _:
                       print("Invalid Option.")

        case "2":
	    
            files_check = {
  		 "html": True,
		 "php":  True,
		 "xml": True,
 		 "txt": False,
                 "json": False,
                 "js": False,
                 "py": False,
                 "pdf": False,
                 "asp": False
            }

            while True:
                
                os.system('clear')
                print("<---- Select File Types ---->")
                
                
                for i, (file, item) in enumerate(files_check.items(), 1):
                    mark = "X" if item else " "
                    print(f"\x1b[33m  [{i}]\x1b[00m  [{mark}] .{file}")
                
                print("\x1b[33m  [0]\x1b[00m  Done (Confirm Selection)")
                
                option = input("\nUse the numbers to select the files you want: ")
                
                if option == "0" or option == "":
                    break 
                
                
                try:
                    idx = int(option) - 1
                    keys = list(files_check.keys())
                    if 0 <= idx < len(keys):
                        file_selected = keys[idx]
                        
                        files_check[file_selected] = not files_check[file_selected]
                except ValueError:
                    pass  

            files = ",".join([file for file, mark in files_check.items() if mark])
            
            if not files:
                files = "php,txt,html"

            while True:
                gobuster_menu()

                gobuster_file = {
                    "1": "Small",
                    "2": "Common",
                    "3": "Big"
                }

                sub = input("\nSelect the scan type: ")
                print(f"-> {gobuster_file.get(sub, 'Invalid Option')}")
                
                match sub:
                    case "1":
                        url = input("Target URL: ")
                        os.system(f"gobuster dir -u {url} -w /usr/share/wordlists/dirb/small.txt -t 50 -q -x {files}")
                   
                    case "2":
                        url = input("Target URL: ")
                        os.system(f"gobuster dir -u {url} -w /usr/share/wordlists/dirb/common.txt -t 50 -q -x {files}")

                    case "3":
                        url = input("Target URL: ")
                        os.system(f"gobuster dir -u {url} -w /usr/share/wordlists/dirb/big.txt -t 50 -q -x {files}")

                    case "0":
                        break

                    case _:
                        print("Invalid Option.")


        case "9":
            print("\n======================================================")
            print(" 👺 HOW DOES GOBLINSCAN WORK? (QUICK GUIDE)")
            print("======================================================")
            print("\n1. THE NETWORK STAGE (Nmap Options)")
            print("   • Scan your local network (e.g., 192.168.1.0/24) to find active devices.")
            print("   • Pick a specific IP and run a stealth scan to see open ports.")
            print("   • Look for web ports like 80 or 443 in the results.")
            print("\n2. THE WEB STAGE (Gobuster Options)")
            print("   • If Nmap reveals a website or an IP running a web service, copy it.")
            print("   • Feed that URL/IP into the Gobuster option.")
            print("   • The tool will use the 'big.txt' wordlist to bruteforce hidden paths.")
            print("\nSUMMARY: First you map the network with Nmap, then you hack the folders with Gobuster!")
            print("======================================================")
            input("\nPress [ENTER] to return to the main menu...")


        case "0":
            print("Exit...")
            break

        case _:
            print("Invalid Option.")
