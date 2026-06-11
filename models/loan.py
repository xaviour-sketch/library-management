class Loan:
    def __init__(
        self,
        loan_id,
        member_id,
        book_id,
        returned=False
    ):
        self.loan_id = loan_id
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