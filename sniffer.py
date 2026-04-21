from scapy.all import sniff, IP, TCP, UDP, DNS
from parser import parse_packet
from redactor import redact_data

def handle(pkt):
    parsed = parse_packet(pkt)
    safe = redact_data(parsed)
    print(safe)

sniff(iface="lo", count=25, prn=handle, filter="tcp or udp")
