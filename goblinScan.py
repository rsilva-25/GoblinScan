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
    print("\x1b[33m[0]\x1b[00m Sair")

def nmap_menu():
    print("<---- nmap Menu ---->")
    print("\x1b[33m[1]\x1b[00m Full Scan")
    print("\x1b[33m[2]\x1b[00m Fast Scan")
    print("\x1b[33m[3]\x1b[00m Port Scan")
    print("\x1b[33m[4]\x1b[00m OS and versions Scan")

banner()

while True:
    menu()
    opcao = input("\nEscolhe uma opção: ")

    match opcao:
        case "1":
            while True:
                nmap_menu()
                sub = input("\nSelect the scan type: ")
                
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
                       print("error")


        case "2":
            url = input("URL alvo: ")
            os.system(f"gobuster dir -u {url} -w /usr/share/wordlists/dirb/big.txt -t 50 -q -x php,txt,html")

        case "0":
            print("A sair...")
            break

        case _:
            print("Opção inválida.")
