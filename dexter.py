import os
import sys
from datetime import datetime

# ANSI Terminal Color Palette
RED = "\033[31m"      # Blood Red
GREEN = "\033[32m"    # Success Green
YELLOW = "\033[33m"   # Warning/Process Yellow
CYAN = "\033[36m"     # Technical Cyan
RESET = "\033[0m"     # Reset to default

def print_banner():
    # Elite Cyber Threat Hunting & Dexter Inspired ASCII Art
    banner = f"""
{RED}    ________  __    _______ ___  ______ 
   /_  __/ / / / __ \/ ____/   |/_  __/ 
    / / / /_/ / /_/ / __/ / /| |  / /    
   / / / __  / _, _/ /___/ ___ | / /     
  /_/ /_/ /_/_/ |_/_____/_/  |_|/_/      
                                         
        {RESET}{CYAN}[+]-- {RED}DEXTER'S DIGITAL KILL ROOM v2.0{CYAN} --[+]{RESET}
        {CYAN}[+]--       STATUS: HUNTING ACTIVE      --[+]{RESET}
    """
    print(banner)

def eliminate_target(target_ip):
    # Secure execution log path
    kill_room_log = "/var/log/dexter_kill_room.log"
    
    print(f"{YELLOW}[*] Preparing the kill room. Laying down the plastic sheets for IP: {target_ip}...{RESET}")
    
    # Kernel-level packet execution via iptables
    # -A INPUT: Append rule to the incoming traffic chain
    # -s: Match the source IP address
    # -j DROP: Immediately discard the packets silently
    command = f"sudo iptables -A INPUT -s {target_ip} -j DROP"
    result = os.system(command)
    
    if result == 0:
        print(f"\n{RED}[☠️] EXECUTION SUCCESSFUL! Target [{target_ip}] has been sliced from the network and dropped into the deep ocean. 🌊{RESET}")
        
        # Logging the artifact disappearance safely
        try:
            with open(kill_room_log, "a") as file:
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{time_now}] [ELIMINATED] -> Source IP: {target_ip} dropped silently.\n")
            print(f"{GREEN}[+] Threat indexed properly in secret log: {kill_room_log}{RESET}\n")
        except PermissionError:
            print(f"{YELLOW}[!] WARNING: Rule applied, but log access denied. Run with full sudo privileges next time.{RESET}\n")
    else:
        print(f"{RED}[-] ERROR: The target {target_ip} slipped away! Check root/sudo permissions.{RESET}\n")

if __name__ == "__main__":
    print_banner()
    if len(sys.argv) < 2:
        print(f"{YELLOW}Usage: sudo python3 dexter.py <TARGET_IP>{RESET}\n")
    else:
        eliminate_target(sys.argv[1])
