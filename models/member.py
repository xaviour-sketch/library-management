from models.person import Person


class Member(Person):
    id_counter = 1

    def __init__(self, name, email):
        super().__init__(name, email)

        self.member_id = Member.id_counter
        Member.id_counter += 1

    def __str__(self):
        return (
            f"Member ID: {self.member_id}, "
            f"Name: {self.name}, "
            f"Email: {self.email}"
        )
    
    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email
        }
    
    @classmethod
    def from_dict(cls, data):
        member = cls(
            data["name"],
            data["email"]
        )

        member.member_id = data["member_id"]

        return member