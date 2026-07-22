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
    print("\n Create by: rsilva25")
def menu():
    print("\n[1] Nmap Scan")
    print("[2] Gobuster Scan")
    print("[0] Sair")

banner()

while True:
    menu()
    opcao = input("\nEscolhe uma opção: ")

    match opcao:
        case "1":
            alvo = input("IP/domínio: ")
            os.system(f"nmap -sV -Pn {alvo}")

        case "2":
            url = input("URL alvo: ")
            wordlist = input("Wordlist: ")
            os.system(f"gobuster dir -u {url} -w {wordlist}")

        case "0":
            print("A sair...")
            break

        case _:
            print("Opção inválida.")
