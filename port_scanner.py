#!/usr/bin/python3
import socket
import sys
import threading

usage = "python3 port_scan.py TARGET START_PORT END_PORT"
print("_" * 70)
print("Python Simple Port Scanner")
print("_" * 70)

if len(sys.argv) != 4:
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning target:", target)

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = s.connect_ex((target, port))
    if not conn:
        print("Port {} is OPEN".format(port))
    s.close()

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.daemon = True
    thread.start()

# Wait for threads to finish
threading.Event().wait()
