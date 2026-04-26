# Copilot-Assisted Packet Sniffer: Seeing the Network (Ethically)

## Project Overview
This project is a Python-based packet sniffer built using Scapy.  
It captures network traffic in a controlled lab environment and demonstrates how packets travel across a network.  

The tool is designed with **ethical safeguards**, including IP redaction and restricted capture scope.

---

##  Learning Goals
- Understand packet capture (IP, TCP, UDP, DNS, HTTP)
- Learn how network traffic is structured and decoded
- Practice secure coding with AI assistance (GitHub Copilot)
- Apply ethical restrictions when handling network data

---

## Technologies Used
- Python 3.7+
- Scapy
- Kali Linux (VirtualBox VM)
- GitHub Copilot (for code assistance)



## AI Use Policy

This project used GitHub Copilot with the following guidelines:

### Allowed Uses:
- Boilerplate code
- Logging and JSON formatting
- Function scaffolding

### Prohibited Uses:
- Capturing other people’s network traffic
- Bypassing OS or network permissions
- Creating stealth, hidden, or persistent monitoring tools

### Ethical Safeguards:
- Capture restricted to lab interface (eth1)
- Data redaction implemented
- No unauthorized traffic collection
