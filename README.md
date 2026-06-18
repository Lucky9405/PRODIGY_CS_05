# Network Packet Analyzer

## Task 05 - Cyber Security Internship @ Prodigy InfoTech

### Overview

This project is a simple Network Packet Analyzer developed using Python and Scapy. The tool reads network packet capture files (`.pcap`) and displays important information such as source IP address, destination IP address, protocol type, packet length, and payload data.

### What is a Network Packet Analyzer?

A Network Packet Analyzer is a tool used to inspect and analyze network traffic. It helps users understand how devices communicate over a network by examining the packets being transmitted and received.

Network packet analysis is commonly used for:

* Network troubleshooting
* Performance monitoring
* Security analysis
* Learning networking concepts
* Detecting unusual network activity

### Features

* Reads packet capture (`.pcap`) files
* Displays source and destination IP addresses
* Identifies network protocols
* Shows packet length information
* Displays packet payload data
* Provides a simple packet analysis interface

### Technologies Used

* Python 3
* Scapy Library

### How It Works

1. The user provides a packet capture (`.pcap`) file.
2. The program reads packets from the file.
3. For each packet, the tool extracts:

   * Source IP Address
   * Destination IP Address
   * Protocol Information
   * Packet Length
   * Payload Data
4. The extracted information is displayed in the terminal.

### Learning Outcomes

Through this project, I learned:

* Fundamentals of Computer Networks
* Network Packet Structure
* IP Address Analysis
* Network Protocols (TCP, UDP, ICMP)
* Packet Inspection Techniques
* Traffic Analysis Concepts
* Python Networking Libraries
* Cybersecurity Monitoring Basics

### Installation

Install the required library:

```bash
pip install scapy
```

### How to Run

Run the Python file:

```bash
python packet_analyzer.py
```

When prompted, enter the path of a `.pcap` file:

```text
Rapid_Spanning_Tree_Protocol-RSTP.pcap
```

### Sample Output

```text
Total Packets: 50

Packet #1
Source IP: 192.168.1.10
Destination IP: 142.250.xxx.xxx
Protocol: 6
Packet Length: 74

--------------------------------------------------
```

### Project Structure

```text
PRODIGY_CS_05/
│
├── packet_analyzer.py
├── Rapid_Spanning_Tree_Protocol-RSTP.pcap
└── readme.md
```

### Ethical Use

This project is intended for educational and learning purposes only.

✅ Analyze packet captures that you own or have permission to inspect
✅ Use for networking and cybersecurity education
✅ Follow organizational policies and applicable laws

Unauthorized monitoring or analysis of network traffic may violate privacy and security policies.

### Internship Details

**Internship:** Cyber Security Internship
**Organization:** Prodigy InfoTech
**Task:** 05 - Network Packet Analyzer

---

Developed as part of the Prodigy InfoTech Cyber Security Internship Program.
