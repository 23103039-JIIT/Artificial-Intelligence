from sympy import symbols
from sympy.logic.boolalg import And, Not

CreditScore, Income, Employment, DTI, Collateral, Repayment = symbols(
    'CreditScore Income Employment DTI Collateral Repayment'
)

loan_approval_rule = And(
    CreditScore,
    Income,
    Employment,
    DTI,
    Collateral,
    Repayment
)

def evaluate_loan(applicant_data):
    result = loan_approval_rule.subs(applicant_data)

    if result:
        print("Loan Approved")
    else:
        print("Loan Rejected")
        print("Reasons for rejection:")
        for criterion, value in applicant_data.items():
            if not value:
                print(f"- {criterion} failed")

ramesh_data = {
    CreditScore: True,      # Credit score ≥ 650
    Income: True,           # Income ≥ INR 8,00,000
    Employment: False,       # Employment ≥ 3 years
    DTI: True,              # Debt-to-income ≤ 40%
    Collateral: True,       # Collateral ≥ 10% loan amount
    Repayment: True         # No defaults in last 2 years
}

evaluate_loan(ramesh_data)