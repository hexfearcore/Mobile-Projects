
#!/usr/bin/env python3

import socket
import threading
import argparse
from colorama import Fore, Style

print(Fore.CYAN + """
  ____             _     ____                                  
 |  _ \ ___   ___ | |_  |  _ \ ___  ___ _ ____   _____ _ __    
 | |_) / _ \ / _ \| __| | |_) / _ \/ _ \ '__\ \ / / _ \ '__|   
 |  __/ (_) | (_) | |_  |  __/  __/  __/ |   \ V /  __/ |      
 |_|   \___/ \___/ \__| |_|   \___|\___|_|    \_/ \___|_|      
                                                             
"""+Style.RESET_ALL)

parser = argparse.ArgumentParser(description="Simple Port Scanner")
parser.add_argument("host", help="Target IP or hostname")
parser.add_argument("-p", "--ports", help="Port range, e.g. 1-100", default="1-1024")

args = parser.parse_args()

host = args.host
port_range = args.ports.split("-")
start_port = int(port_range[0])
end_port = int(port_range[1])

print(f"\nScanning host: {host}")
print(f"Port range: {start_port} to {end_port}\n")

def scan(port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((host, port))
        print(Fore.GREEN + f"[+] Port {port} is OPEN" + Style.RESET_ALL)
        sock.close()
    except:
        pass

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan, args=(port,))
    t.start()
