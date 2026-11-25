
def recommend_tool(task):
    task = task.lower()

    tools = {
        "Wireshark": [
            "packet", "network traffic", "protocol", "sniffing"
        ],
        "Nmap": [
            "port scan", "open ports", "network discovery"
        ],
        "Splunk": [
            "log analysis", "siem", "security events", "monitoring"
        ],
        "Metasploit": [
            "penetration testing", "exploit", "vulnerability testing"
        ],
        "Nessus": [
            "vulnerability scan", "security assessment", "weakness"
        ],
        "Snort": [
            "intrusion detection", "ids", "suspicious traffic"
        ]
    }

    scores = {}

    for tool, keywords in tools.items():
        scores[tool] = sum(
            1 for keyword in keywords if keyword in task
        )

    best_tool = max(scores, key=scores.get)

    if scores[best_tool] == 0:
        return "No suitable tool found"

    return best_tool


task = input("Enter security task description: ")

result = recommend_tool(task)

print("\n--- Security Tool Recommendation ---")
print("Task:", task)
print("Recommended Tool:", result)
