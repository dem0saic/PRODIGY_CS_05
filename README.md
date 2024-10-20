# PRODIGY_CS_05
 Develop a packet sniffer tool that captures and analyzes network packets. Display relevant information such as source and destination IP addresses, protocols, and payload data. Ensure the ethical use of the tool for educational purposes.

# Network Packet Analyzer

## Overview
The **Network Packet Analyzer** is a Python program that captures and analyzes TCP packets on a specified network interface. It extracts the source and destination IP addresses, source and destination ports, and raw data from each packet. The packet information is displayed on the console and written to a log file.

## Features
- Captures TCP packets on a specified network interface.
- Displays source and destination IP addresses and ports.
- Logs packet information and raw data to a text file.
- Colorful console output for better readability.

## Requirements
- `Python 3.x`
- `Scapy`
- `PyFiglet`
- `Termcolor`
- `Npcap` (for Windows users)

## Installation
1. **Install Python**: Make sure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. **Install Required Libraries**: Use pip to install the necessary libraries:
   ```bash
   pip install scapy pyfiglet termcolor
Install Npcap (Windows only): Download and install Npcap from Npcap Official Website. During installation, select the option "Install Npcap in WinPcap API-compatible Mode".

# Usage
To run the packet analyzer, use the following command in your terminal or command prompt:
`
```python Network-Packet-Analyzer.py <interface> [verbose]``
Replace <interface> with the name of the network interface you want to sniff on (e.g., Wi-Fi, Ethernet).
The optional verbose parameter can be added to display more detailed output.

# Example Command
bash
```
python Network-Packet-Analyzer.py Wi-Fi verbose
```

# Code Explanation
The program uses Scapy to sniff packets and extract relevant information. Here’s a brief overview of the main components:

handle_packet(packet, log): This function processes each captured packet, extracting TCP layer details and writing them to the log file.
main(interface, verbose): This function initializes the packet sniffing process on the specified interface and handles logging.
Colorful Output: The program uses PyFiglet and Termcolor to create a visually appealing title and output.
Creator
Created by: Dem0saic
GitHub: dem0saic
LinkedIn: owusuvincent

License
This project is licensed under the MIT License - see the LICENSE file for details.

### Instructions
1. **Create a new file**: Open your text editor or IDE and create a new file named `README.md`.
2. **Copy and paste the content**: Copy the above markdown content and paste it into your `README.md` file.
3. **Save the file**: Save the changes to the file.




