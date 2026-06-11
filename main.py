from models.member import Member

member1 = Member(
    "John",
    "john@gmail.com"
)

member2 = Member(
    "Mary",
    "mary@gmail.com"
)

print(member1)
print(member2)

print("\nNext Member ID:", Member.id_counter)
