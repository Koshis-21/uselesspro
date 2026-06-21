import socket

print("=" * 40)
print("Simple Port Scanner")
print("=" * 40)

target = input("Enter target IP (example: 127.0.0.1): ")

common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443]

print(f"\nScanning {target}...\n")

for port in common_ports: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")

    sock.close()

print("\nScan Complete.")