import socket 
import os

host = input("enter target IP or domain:")
print("\n checking the host availability...")
response = os.system("ping -n 1" +host)

if response == 0:
    print("Host is Reachable..")
else:
    print("Host is NOT reachable..")

print("\nScanning common ports...")

common_ports = [22, 80]

for port in common_ports:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    result = s.connect_ex((host,port))
if result == 0:
    print(f"port{port}is OPEN")
else:
    print(f"port{port}is CLOSED")
s.close()            
