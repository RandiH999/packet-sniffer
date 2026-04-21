def parse_packet(pkt):
    data = {}

    if pkt.haslayer("IP"):
        data["src_ip"] = pkt["IP"].src
        data["dst_ip"] = pkt["IP"].dst

    if pkt.haslayer("TCP"):
        data["protocol"] = "TCP"
    elif pkt.haslayer("UDP"):
        data["protocol"] = "UDP"

    if pkt.haslayer("DNS") and pkt.getlayer("DNS").qd:
        data["dns"] = pkt["DNS"].qd.qname.decode()

    return data
