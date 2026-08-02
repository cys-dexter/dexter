from datetime import datetime
import ipaddress
import os
import sys
import warnings

# منع تحذيرات بايثون بشكل نهائي
warnings.filterwarnings("ignore", category=SyntaxWarning)

# ANSI Terminal Color Palette
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

BANNED_REPO_FILE = "banned_ips.txt"


def print_banner():
    banner = fr"""
{RED}    ________  __     _______ ___  ______ 
   /_  __/ / / / __ \/ ____/   |/_  __/ 
    / / / /_/ / /_/ / __/ / /| |  / /    
   / / / __  / _, _/ /___/ ___ | / /     
  /_/ /_/ /_/_/ |_/_____/_/  |_|/_/      
                                         
        {RESET}{CYAN}[+]-- {RED}DEXTER'S DIGITAL KILL ROOM v2.2{CYAN} --[+]{RESET}
        {CYAN}[+]--     CREATOR: AHMAD | CYS-DEXTER    --[+]{RESET}
        {CYAN}[+]--     GITHUB: cys-dexter             --[+]{RESET}
        {CYAN}[+]--        STATUS: HUNTING ACTIVE      --[+]{RESET}
    """
    print(banner)


def is_valid_ip(ip_str):
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False


def save_to_banned_repository(target_ip):
    try:
        banned_list = []
        if os.path.exists(BANNED_REPO_FILE):
            with open(BANNED_REPO_FILE, "r") as f:
                banned_list = [line.strip() for line in f if line.strip()]

        if target_ip in banned_list:
            return False

        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(BANNED_REPO_FILE, "a") as f:
            f.write(f"{target_ip} # Banned on {time_now}\n")
        return True
    except Exception:
        return False


def eliminate_target(target_ip):
    if not is_valid_ip(target_ip):
        print(f"{RED}[-] ERROR: [{target_ip}] is not a valid IP address! Check your input.{RESET}\n")
        return

    kill_room_log = "/var/log/dexter_kill_room.log"

    print(f"{YELLOW}[*] Preparing the kill room. Laying down the plastic sheets for IP: {target_ip}...{RESET}")

    command = f"sudo iptables -A INPUT -s {target_ip} -j DROP"
    result = os.system(command)

    if result == 0:
        print(f"\n{RED}[☠️] EXECUTION SUCCESSFUL! Target [{target_ip}] has been sliced from the network and dropped into the deep ocean. 🌊{RESET}")

        repo_updated = save_to_banned_repository(target_ip)
        if repo_updated:
            print(f"{GREEN}[+] IP successfully added to local repository: {BANNED_REPO_FILE}{RESET}")
        else:
            print(f"{YELLOW}[!] Note: IP was dropped, but it was already recorded in the repository.{RESET}")

        try:
            with open(kill_room_log, "a") as file:
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{time_now}] [ELIMINATED] -> Source IP: {target_ip} dropped silently.\n")
            print(f"{GREEN}[+] Threat indexed properly in system log: {kill_room_log}{RESET}\n")
        except PermissionError:
            print(f"{YELLOW}[!] WARNING: Rule applied, but system log access denied.{RESET}\n")
    else:
        print(f"{RED}[-] ERROR: The target {target_ip} slipped away! Ensure you are running with sudo/root privileges.{RESET}\n")


if __name__ == "__main__":
    if os.geteuid() != 0:
        print(f"{RED}[!] SECURITY NOTICE: This tool requires root privileges to manipulate iptables.{RESET}")
        print(f"{YELLOW}[*] Please run as: sudo python3 dexter.py <IP>{RESET}\n")
        sys.exit(1)

    print_banner()

    if len(sys.argv) < 2:
        print(f"{YELLOW}Usage: sudo python3 dexter.py <TARGET_IP>{RESET}\n")
        if os.path.exists(BANNED_REPO_FILE):
            print(f"{CYAN}[*] Current Banned IPs Repository ({BANNED_REPO_FILE}):{RESET}")
            with open(BANNED_REPO_FILE, "r") as f:
                print(f"{GREEN}{f.read()}{RESET}")
    else:
        eliminate_target(sys.argv[1])
