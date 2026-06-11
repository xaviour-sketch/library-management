class Loan:
    id_counter = 1

    def __init__(self, member_id, book_id, returned=False):
        self.loan_id = Loan.id_counter
        Loan.id_counter += 1

        self.member_id = member_id
        self.book_id = book_id
        self.returned = returned

    def __str__(self):
        status = "Returned" if self.returned else "Borrowed"

        return (
            f"Loan ID: {self.loan_id}, "
            f"Member ID: {self.member_id}, "
            f"Book ID: {self.book_id}, "
            f"Status: {status}"
        )
    
    def to_dict(self):
        return {
            "loan_id": self.loan_id,
            "member_id": self.member_id,
            "book_id": self.book_id,
            "returned": self.returned
        }