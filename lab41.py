from sympy.logic.boolalg import Or, And, Not, Implies, Equivalent
from sympy import symbols, satisfiable

# Define propositional variables
SoreThroat = symbols('SoreThroat')
Headache = symbols('Headache')
Fever = symbols('Fever')
CommonCold = symbols('CommonCold')
Flu = symbols('Flu')
BedRest = symbols('BedRest')
Fluids = symbols('Fluids')

facts = {SoreThroat:True, Headache:True}

rules = [
    Implies(And(SoreThroat, Headache), CommonCold),
    Implies(And(Fever, Headache), Flu),
    Implies(CommonCold, BedRest),
    Implies(Flu, Fluids)
]

knowledge_base = facts.copy()

while True:
    new_inferences = {}
    for rule in rules:
        premise, conclusion = rule.args
        # Evaluate the premise with current knowledge
        if isinstance(premise, And):
            premise_truth = all(knowledge_base.get(arg, False) for arg in premise.args)
        else:
            knowledge_base.get(premise, False)

        if premise_truth and conclusion not in knowledge_base:
            new_inferences[conclusion] = True

    if not new_inferences: 
        break

    knowledge_base.update(new_inferences)

conclusions = []

if knowledge_base.get(CommonCold, False):
    conclusions.append("The patient may have a common cold.")

if knowledge_base.get(Flu, False): 
    conclusions.append("The patient may have the flu.")

recommendations = []

if knowledge_base.get(CommonCold, False):
    recommendations.append("Recommend bed rest.")

if knowledge_base.get(Flu, False):
    recommendations.append("Recommend plenty of fluids.")

# Output the conclusions and recommendations
print("Conclusions:")
for conclusion in conclusions:
    print(conclusion)

print("\nRecommendations:")
for recommendation in recommendations:
    print(recommendation)
