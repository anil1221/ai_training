def human_approval(action):
    print("\nHuman Approval Required")
    print(f"Action: {action}")
    response = input("Approve? (yes/no): ")

    return response.lower() == "yes"