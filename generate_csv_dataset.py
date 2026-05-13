import os
import pandas as pd
import random

# CREATE FOLDER
os.makedirs("datasets/finance", exist_ok=True)

finance_data = []

departments = [
    "Finance",
    "HR",
    "Operations",
    "Sales",
    "Marketing"
]

for i in range(1, 501):

    finance_data.append({
        "employee_id": i,
        "department": random.choice(departments),
        "quarter": random.choice(["Q1", "Q2", "Q3", "Q4"]),
        "revenue": random.randint(100000, 5000000),
        "profit": random.randint(50000, 1000000),
        "expenses": random.randint(10000, 500000),
        "bonus": random.randint(1000, 50000)
    })

df = pd.DataFrame(finance_data)

df.to_csv(
    "datasets/finance/finance_reports.csv",
    index=False
)

print("500 CSV rows generated successfully")
