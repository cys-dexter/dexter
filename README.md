# 🔪 Dexter's Digital Kill Room (cys-dexter)

> **Creator:** Ahmad | CYS-Dexter  
> **GitHub:** [cys-dexter](https://github.com/cys-dexter)  
> **Status:** Hunting Active  

A specialized, lightweight Python script designed for elite cyber threat hunting and incident response. It interacts directly with the Linux kernel via `iptables` to silently drop and isolate malicious incoming IP addresses, inspired by the digital forensics workflow and the aesthetic of Dexter.

---

### ⚙️ Features
* **Kernel-Level Isolation:** Instantly drops incoming packets from a target IP using native `iptables`.
* **Strict IP Validation:** Built-in verification logic to ensure proper IPv4/IPv6 syntax before rule execution.
* **Local Banned Repository:** Automatically maintains and logs all eliminated IPs (`banned_ips.txt`) with timestamps to prevent duplicate rules and track history.
* **Atmospheric CLI Interface:** Clean, ANSI-colored terminal dashboard optimized for high-visibility threat management.

---

### 🚀 Installation & Usage

#### 1. Clone the Repository
Open your terminal and run the following commands to clone the repository and navigate into its directory:

```bash
git clone [https://github.com/cys-dexter/cys-dexter.git](https://github.com/cys-dexter/cys-dexter.git)
cd cys-dexter
2. Execute the Tool
Because this script modifies system-level firewall rules via iptables, it must be executed with root (sudo) privileges:

Bash
sudo python3 dexter.py <TARGET_IP>
Example for blocking a suspicious IP:

Bash
sudo python3 dexter.py 192.168.1.100
3. View Banned IPs Repository
To review all previously targeted and locally stored banned IP addresses along with their timestamps, run the script without any arguments:

Bash
sudo python3 dexter.py
📂 File Structure
dexter.py - The core script containing the logic, IP validation, and ANSI interface.

banned_ips.txt - Local log repository tracking all previously blocked targets (auto-generated upon first successful ban).

⚠️ Disclaimer
This tool is intended for educational, authorized defensive security, and incident response purposes only. Use responsibly in controlled environments.
