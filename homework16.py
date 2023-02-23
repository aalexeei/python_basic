# Define the Person class
class Person:
    """
    Класс описывающий человека
    """
    __firstname = str()
    __lastname = str()
    __age = int()
    __email = str()
    __phone = str()

    @property
    def firstname(self):
        return self.__firstname.capitalize()

    @property
    def lastname(self):
        return self.__lastname.capitalize()

    @property
    def age(self):
        return self.__age

    @property
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone

    @email.setter
    def email(self, email: str):
        self.__email = email

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    def __set_age(self, age: int):
        if age >= 0:
            self.__age = age
        else:
            self.__age = 0

    def __init__(self, name: str, surname: str, age: int):
        self.__firstname = name
        self.__lastname = surname
        self.__set_age(age)

    def __str__(self):
        info = f'Name: {self.firstname}\nSurname: {self.lastname}\nAge: {self.age}\n'
        if self.email != '':
            info = f'{info}e-mail: {self.email}\n'
        if self.phone != '':
            info = f'{info}phone: {self.phone}'
        return info


# Define the Family class
class Family:
    """
    Класс описывающий семью, содержащую экземпляры класса Person
    """

    def __init__(self, members: list):
        self.members = members

    def add_member(self, member: Person):
        self.members.append(member)

    def remove_member(self, member: Person):
        self.members.remove(member)

    def get_oldest_member(self) -> Person:
        oldest_member = None
        for member in self.members:
            if oldest_member is None or member.age > oldest_member.age:
                oldest_member = member
        return oldest_member

    def get_youngest_member(self) -> Person:
        youngest_member = None
        for member in self.members:
            if youngest_member is None or member.age < youngest_member.age:
                youngest_member = member
        return youngest_member

    def get_family_members(self):
        for member in self.members:
            print(member)


# Create some Person objects
person1 = Person('John', 'Doe', 25)
person2 = Person('Jane', 'Doe', 30)
person3 = Person('Bob', 'Smith', 50)

# Create a Family object containing those Person objects
family = Family([person1, person2, person3])

# Add a new member to the family
person4 = Person('Alice', 'Jones', 20)
family.add_member(person4)

# Print out information about the family members
family.get_family_members()

# Get the oldest and youngest members of the family
oldest_member = family.get_oldest_member()
youngest_member = family.get_youngest_member()
print(f'The oldest family member is {oldest_member.firstname} {oldest_member.lastname}')
print(f'The youngest family member is {youngest_member.firstname} {youngest_member.lastname}')
