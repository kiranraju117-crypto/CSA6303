
def classify_alert(alert):

    alert = alert.lower()

    if any(word in alert for word in
           ["ransomware", "data breach", "active attack",
            "critical server compromised"]):
        return "P1 - Critical"

    elif any(word in alert for word in
             ["malware", "unauthorized access",
              "multiple failed logins", "privilege escalation"]):
        return "P2 - High"

    elif any(word in alert for word in
             ["suspicious login", "port scanning",
              "unusual traffic", "phishing email"]):
        return "P3 - Medium"

    else:
        return "P4 - Low"


print("SOC ALERT PRIORITY CLASSIFICATION")
print("--")

alert = input("Enter SOC Alert Description: ")

priority = classify_alert(alert)

print("\nAlert Description:", alert)
print("Assigned Priority:", priority)
