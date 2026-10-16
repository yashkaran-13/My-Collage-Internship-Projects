"""
Port Scanner (Educational / Defensive Use Only)
-----------------------------------------------
Scans a target host for open TCP ports using sockets.
Only scan systems you own or have explicit permission to test.

Usage:
    python port_scanner.py <target> [start_port] [end_port]

Example:
    python port_scanner.py 127.0.0.1 1 1024
"""

import socket
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# Well-known ports for quick identification
COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS",
    445: "SMB", 3306: "MySQL", 3389: "RDP", 8080: "HTTP-Alt",
}


def resolve_target(target: str) -> str:
    """Convert a hostname to an IP address."""
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        print(f"[!] Could not resolve hostname: {target}")
        sys.exit(1)


def scan_port(ip: str, port: int, timeout: float = 0.5) -> bool:
    """Return True if the port is open."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            if s.connect_ex((ip, port)) == 0:
                return True
    except socket.error:
        pass
    return False


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    target = sys.argv[1]
    start_port = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    end_port   = int(sys.argv[3]) if len(sys.argv) > 3 else 1024

    ip = resolve_target(target)
    print("-" * 50)
    print(f"Target : {target} ({ip})")
    print(f"Ports  : {start_port} - {end_port}")
    print(f"Time   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    open_ports = []

    def worker(port):
        if scan_port(ip, port):
            service = COMMON_PORTS.get(port, "Unknown")
            open_ports.append((port, service))
            print(f"[OPEN] Port {port:<6} -> {service}")

    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(worker, range(start_port, end_port + 1))

    print("-" * 50)
    if open_ports:
        print(f"Scan complete. {len(open_ports)} open port(s) found.")
    else:
        print("Scan complete. No open ports found in the given range.")
    print("-" * 50)


if __name__ == "__main__":
    main()
