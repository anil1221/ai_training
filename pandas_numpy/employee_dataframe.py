import pandas as pd
import numpy as np

# Generate employee data
employee_data = [
    {
        "empid": 101,
        "emp_name": "Anil",
        "salary": 120000,
        "department": "AI",
        "skillset": ["Python", "GenAI", "FastAPI"],
        "assignedornot": True,
        "client_name": "Google"
    },
    {
        "empid": 102,
        "emp_name": "Rahul",
        "salary": 95000,
        "department": "Backend",
        "skillset": ["Java", "Spring", "SQL"],
        "assignedornot": False,
        "client_name": None
    },
    {
        "empid": 103,
        "emp_name": "Sneha",
        "salary": 150000,
        "department": "AI",
        "skillset": ["Python", "GenAI", "LangChain"],
        "assignedornot": True,
        "client_name": "Microsoft"
    },
    {
        "empid": 104,
        "emp_name": "Kiran",
        "salary": 85000,
        "department": "Data",
        "skillset": ["Python", "Pandas", "NumPy"],
        "assignedornot": True,
        "client_name": "Amazon"
    },
    {
        "empid": 105,
        "emp_name": "Priya",
        "salary": 99000,
        "department": "Backend",
        "skillset": ["Python", "Django", "PostgreSQL"],
        "assignedornot": True,
        "client_name": "Google"
    },
    {
        "empid": 106,
        "emp_name": "Arjun",
        "salary": 175000,
        "department": "AI",
        "skillset": ["Transformers", "GenAI", "Python"],
        "assignedornot": False,
        "client_name": None
    }
]

# Create dataframe
df = pd.DataFrame(employee_data)

print("\nEMPLOYEE DATAFRAME")
print(df)



# highest salary empoyees per department
highest_salary_idx = df.groupby("department")["salary"].idxmax()

highest_salary_employees = df.loc[
    highest_salary_idx,
    ["department", "emp_name", "salary"]
]
print("\n Highest Salary Employee Per Department")
print(highest_salary_employees)

# GenAI employees assigned to clients
genai_assigned = df[
    df["skillset"].apply(lambda skills: "GenAI" in skills)
    &
    (df["assignedornot"] == True)
]

print("\n GenAI employees assigned to clients")
print(genai_assigned[["emp_name", "department", "client_name"]])



# Add skill to summary column
df["skill_summary"] = df["skillset"].apply(
    lambda skills: ", ".join(skills)
)
print("\n Add skill to summary column")
print(df[["emp_name", "skill_summary"]])


# employees with python skill")
python_employees = df[
    df["skillset"].apply(
        lambda skills: "Python" in skills
    )
]
print("\n employees with python skill")
print(python_employees[["emp_name", "salary"]])


# manager report
total_employees = len(df)

assigned_count = df["assignedornot"].sum()

employees_per_client = (
    df[df["assignedornot"] == True]
    .groupby("client_name")
    .size()
    .reset_index(name="employee_count")
)

print(f"\ntotal employees: {total_employees}")
print(f"assigned employees: {assigned_count}")

print("\n employees per client")
print(employees_per_client)