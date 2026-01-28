rules = [
    {
        "if": {"performance": "excellent", "experience": 5},
        "then": "promote",
        "explanation": "Employee has excellent performance and sufficient experience."
    },
    {
        "if": {"performance": "good", "experience": 7},
        "then": "promote",
        "explanation": "Employee has good performance with long experience."
    },
    {
        "if": {"performance": "average"},
        "then": "do_not_promote",
        "explanation": "Employee performance is average."
    }
]

facts = {}
explanations = []

facts["performance"] = input("Enter performance (excellent/good/average): ").lower()
facts["experience"] = int(input("Enter years of experience: "))

decision = None

for rule in rules:
    conditions_met = True

    for key, value in rule["if"].items():
        if key == "experience":
            if facts.get(key, 0) < value:
                conditions_met = False
        else:
            if facts.get(key) != value:
                conditions_met = False

    if conditions_met:
        decision = rule["then"]
        explanations.append(rule["explanation"])


print("\nResult:")
if decision == "promote":
    print("Employee should be PROMOTED.")
elif decision == "do_not_promote":
    print("Employee should NOT be promoted.")
else:
    print("No rule matched. Decision cannot be made.")
    
print("\nExplanation:")
for exp in explanations:
    print("-", exp)
