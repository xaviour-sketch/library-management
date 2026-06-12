class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    # @property (getter) allows us to access email as an attribute.
    # getter is a method that controls how a value is retrieved.    
    @property
    def email(self):
        return self._email

    # @email.setter ensures that the email address is valid when setting it.
    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        self._email = value

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"