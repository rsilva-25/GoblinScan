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
    print("\n\x1b[33m[1]\x1b[00m  Nmap Scan")
    print("\x1b[33m[2]\x1b[00m Gobuster Scan")
    print("\x1b[33m[0]\x1b[00m Sair")

def nmap_menu():
    print("<---- nmap Menu ---->")
    print("[1] Fast Scan")
    print("[2] Full Scan")
    print("[3] Port Scan")
    print("[4] OS and versions Scan")

banner()

while True:
    menu()
    opcao = input("\nEscolhe uma opção: ")

    match opcao:
        case "1":
            while True:
                nmap_menu()
                sub = input("\n Select the scan type: ")
                
                match sub:
                    case "1":
                        target = input("IP/Domain: ")
                        os.system(f"nmap -T4 {target}")

                    case "0":
                        break

                    case _:
                       print("error")
#            alvo = input("IP/domínio: ")
#            os.system(f"nmap -sV -Pn {alvo}")

        case "2":
            url = input("URL alvo: ")
            wordlist = input("Wordlist: ")
            os.system(f"gobuster dir -u {url} -w {wordlist}")

        case "0":
            print("A sair...")
            break

        case _:
            print("Opção inválida.")
