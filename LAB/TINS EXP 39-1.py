
raw_iocs = [
    {"type": "IP", "value": "192.168.1.10"},
    {"type": "DOMAIN", "value": "malicious.com"},
    {"type": "IP", "value": "10.0.0.5"}
]

internal_logs = [
    {"source": "192.168.1.10", "event": "Login Attempt"},
    {"source": "192.168.1.20", "event": "Normal Traffic"},
    {"source": "malicious.com", "event": "DNS Request"},
    {"source": "10.0.0.8", "event": "File Access"}
]

def normalize_iocs(iocs):
    normalized = []

    for ioc in iocs:
        normalized.append({
            "type": ioc["type"].lower(),
            "value": ioc["value"].lower().strip()
        })

    return normalized


def correlate_logs(iocs, logs):
    print("\n--- TIP Correlation Results ---")

    matches = 0

    for log in logs:
        for ioc in iocs:
            if log["source"].lower().strip() == ioc["value"]:
                print("ALERT: Threat Indicator Matched!")
                print("IOC Type:", ioc["type"])
                print("IOC Value:", ioc["value"])
                print("Event:", log["event"])
                print()
                matches += 1

    if matches == 0:
        print("No threat indicators matched.")


print("--- Normalized Threat Indicators ---")

normalized_iocs = normalize_iocs(raw_iocs)

for ioc in normalized_iocs:
    print(ioc)

correlate_logs(normalized_iocs, internal_logs)
