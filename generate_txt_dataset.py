import os
import random

os.makedirs("datasets/hr", exist_ok=True)
os.makedirs("datasets/technical", exist_ok=True)

hr_templates = [
    "Employees are entitled to {} paid leaves annually.",
    "Remote work is allowed {} days per week.",
    "Medical insurance covers {} family members.",
    "Performance reviews occur every {} months.",
    "Employees receive {} bonus during appraisal."
]

technical_templates = [
    "Kubernetes cluster {} experienced {} minutes downtime.",
    "Backup completed successfully at {} AM.",
    "Server CPU usage reached {} percent.",
    "Database replication lag was {} seconds.",
    "Security patch version {} deployed successfully."
]

for i in range(1, 251):

    content = ""

    for _ in range(20):

        sentence = random.choice(hr_templates).format(
            random.randint(1, 30)
        )

        content += sentence + "\n"

    with open(f"datasets/hr/hr_doc_{i}.txt", "w") as f:
        f.write(content)

for i in range(1, 251):

    content = ""

    for _ in range(20):

        sentence = random.choice(technical_templates).format(
            random.randint(1, 20),
            random.randint(1, 60),
            random.randint(1, 24),
            random.randint(50, 100),
            random.randint(1, 500)
        )

        content += sentence + "\n"

    with open(f"datasets/technical/tech_doc_{i}.txt", "w") as f:
        f.write(content)

print("500 TXT documents generated successfully")
