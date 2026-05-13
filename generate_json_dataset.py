import os
import json
import random
from datetime import datetime, timedelta

# CREATE FOLDER
os.makedirs("datasets/logs", exist_ok=True)

logs = []

events = [
    "Unauthorized access attempt",
    "Database backup completed",
    "Server restarted",
    "User login failed",
    "Firewall rule updated",
    "Malware scan completed",
    "Password changed",
    "API access denied",
    "Security patch applied",
    "Audit completed"
]

severity_levels = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

base_date = datetime.now()

for i in range(1, 501):

    random_date = base_date - timedelta(
        days=random.randint(1, 365)
    )

    logs.append({
        "log_id": i,
        "timestamp": str(random_date),
        "event": random.choice(events),
        "severity": random.choice(severity_levels),
        "server_id": random.randint(1000, 5000),
        "user_id": random.randint(1, 1000),
        "ip_address": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}"
    })

with open(
    "datasets/logs/security_logs.json",
    "w"
) as f:

    json.dump(logs, f, indent=4)

print("500 JSON records generated successfully")
