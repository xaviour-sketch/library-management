from models.loan import Loan

loan1 = Loan(1, 101)
loan2 = Loan(2, 102)

print(loan1)
print(loan2)

print("\nNext Loan ID:", Loan.id_counter)
