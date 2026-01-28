# Fault Diagnosis using Resolution Refutation

clauses = [
    {"~power", "machine_fault"},  # ¬power OR machine_fault
    {"power"},                    # power
    {"~machine_fault"}            # negated goal
]

def negate(literal):
    """Return negation of a literal"""
    return literal[1:] if literal.startswith("~") else "~" + literal

def resolve(c1, c2):
    """Resolve two clauses"""
    for literal in c1:
        if negate(literal) in c2:
            resolvent = (c1 - {literal}) | (c2 - {negate(literal)})
            return resolvent
    return None

def resolution_refutation(clauses):
    """Apply resolution refutation"""
    new = set()

    while True:
        pairs = [(clauses[i], clauses[j])
                 for i in range(len(clauses))
                 for j in range(i + 1, len(clauses))]

        for (c1, c2) in pairs:
            resolvent = resolve(c1, c2)
            if resolvent is not None:
                print(f"Resolved {c1} and {c2} → {resolvent}")
                if len(resolvent) == 0:
                    print("\nEmpty clause derived.")
                    print("Machine fault is logically inferred.")
                    return True
                new.add(frozenset(resolvent))

        if new.issubset(set(map(frozenset, clauses))):
            print("\nNo contradiction found.")
            return False

        for clause in new:
            if set(clause) not in clauses:
                clauses.append(set(clause))

resolution_refutation(clauses)