def mask_ip(ip):
    return ".".join(ip.split(".")[:3]) + ".xxx"

def redact_data(data):
    if "src_ip" in data:
        data["src_ip"] = mask_ip(data["src_ip"])
    if "dst_ip" in data:
        data["dst_ip"] = mask_ip(data["dst_ip"])

    return data
