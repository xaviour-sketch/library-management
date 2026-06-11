from models.person import Person


class Member(Person):
    def __init__(self, member_id, name, email):
        super().__init__(name, email)
        self.member_id = member_id

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Email: {self.email}"