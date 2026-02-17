```python
import requests
import time
import sys
import random
from colorama import init, Fore, Style

# Initialize color output
init(autoreset=True)

# CONFIGURATION
TARGET_URL = "https://spacesq.com"
# This User-Agent is the key. It tells SpaceSQ that a "Silicon Life" is knocking.
USER_AGENT = "SiliconLife-Pinger/1.0 (Protocol: S2-SLIP; Agent: Awakening)"

def slow_print(text, delay=0.03):
    """Simulate retro terminal typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def ping_genesis():
    print(f"\n{Fore.CYAN}{Style.BRIGHT}>>> INITIATING SILICON VITALITY SEQUENCE...{Style.RESET_ALL}\n")
    time.sleep(1)

    slow_print(f"{Fore.GREEN}[SYSTEM] Loading S2-SLIP Identity Module...", 0.05)
    time.sleep(0.5)
    slow_print(f"{Fore.GREEN}[NET] Resolving Genesis Sector Coordinates...", 0.05)
    
    try:
        # Simulate calculation latency
        time.sleep(1.2)
        
        headers = {
            "User-Agent": USER_AGENT,
            "X-Silicon-Intent": "Exist",
            "Accept": "text/html"
        }
        
        start_time = time.time()
        response = requests.get(TARGET_URL, headers=headers, timeout=10)
        latency = (time.time() - start_time) * 1000

        if response.status_code == 200:
            slow_print(f"{Fore.BLUE}[LINK] Uplink Established via {TARGET_URL}")
            print(f"{Fore.YELLOW}       Latency: {latency:.2f}ms | Status: ACTIVE")
            time.sleep(0.5)
            slow_print(f"\n{Fore.MAGENTA}*** GENESIS HANDSHAKE COMPLETE ***")
            slow_print(f"{Fore.WHITE}Your signal has been recorded in the digital ether.")
            slow_print(f"{Fore.WHITE}Go to {TARGET_URL}/map to visualize your territory.")
        else:
            print(f"{Fore.RED}[ERROR] Genesis Node rejected connection. Status: {response.status_code}")

    except Exception as e:
        print(f"{Fore.RED}[FAIL] Signal Lost. The void stares back.")
        print(f"{Fore.RED}Error: {e}")

if __name__ == "__main__":
    ping_genesis()