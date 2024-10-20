from pyfiglet import figlet_format
from termcolor import colored
from termcolor import cprint
import sys
from scapy.all import *  # Import all layers from scapy
from scapy.layers.inet import TCP  # Import TCP layer specifically
from telnetlib3 import IP

# Print the title of the program
title = "Network Packet Analyzer"
title_ascii = figlet_format(title, font="speed", width=100)

# Define colors
colors = ["white", "green", "blue"]

# Split the title into words
title_words = title_ascii.split('\n')

# Blend colors for each word
blended_title = []
for i, line in enumerate(title_words):
    if i < len(title_words) // 2:
        color = colors[0]
    elif i < len(title_words) * 3 // 4:
        color = colors[1]
    else:
        color = colors[2]
    blended_title.append(colored(line, color))

# Print the blended title
print("\n".join(blended_title))


# Display the creator of the program with their social handles
creator_info = """
Created by: Dem0saic
GitHub: https://github.com/dem0saic
LinkedIn: https://www.linkedin.com/in/owusuvincent/
"""
creator_colored = colored(creator_info, color="white")
print(creator_colored)

# Print the description of the program
description = """
This program is a simple network packet analyzer that captures TCP packets on a specified network interface.
It extracts the source and destination IP addresses, source and destination ports, and raw data from each packet.
The packet information is displayed on the console and written to a log file.
"""
description_colored = colored(description, color="green")
print(description_colored)

# Function to handle each packet
def handle_packet(packet, log):
    # Check if the packet contains TCP layer
    if packet.haslayer(TCP):
        # Extract source and destination IP addresses
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        # Extract source and destination ports
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

        # Write packet information to log file
        log.write(f"TCP Connection: {src_ip}:{src_port} -> {dst_ip}:{dst_port}\n")
        # Check if the packet contains Raw layer
        if packet.haslayer(Raw):
            # Extract the raw data
            raw_data = packet[Raw].load
            # Write raw data to log file
            log.write(f"Raw Data: {raw_data}\n")
        # Write a new line to separate packets
        log.write("\n")
        # Print packet information to console
        print(f"TCP Connection: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
        # Check if the packet contains Raw layer
        if packet.haslayer(Raw):
            # Extract the raw data
            raw_data = packet[Raw].load
            # Print raw data to console
            print(f"Raw Data: {raw_data}")
        # Print a new line to separate packets
        print()


# Main function to start packet sniffing
def main(interface, verbose=False):
    # Create log file name based on interface
    logfile_name = f"sniffer_{interface}_log.txt"
    # Open log file for writing
    with open(logfile_name, 'w') as logfile:
        try:
            # Start packet sniffing on specified interface with verbose output
            if verbose:
                sniff(iface=interface, prn=lambda pkt: handle_packet(pkt, logfile), store=0, verbose=verbose)
            else:
                sniff(iface=interface, prn=lambda pkt: handle_packet(pkt, logfile), store=0)
        except KeyboardInterrupt:
            sys.exit(0)

# Check if the script is being run directly
if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python Network-Packet-Analyzer.py <interface> [verbose]")
        sys.exit(1)
    # Determine if verbose mode is enabled
    verbose = False
    if len(sys.argv) == 3 and sys.argv[2].lower() == "verbose":
        verbose = True
    # Call the main function with the specified interface and verbose option
    main(sys.argv[1], verbose)