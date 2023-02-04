import json


class Employee:
    def __init__(self, number: int, firstname: str, lastname: str, age: int, e_mail: str, skills: str,
                 people_lang: list, coding_lang: list):
        self.number = number
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.e_mail = e_mail
        self.skills = skills
        self.people_lang = people_lang
        self.coding_lang = coding_lang

    def __str__(self):
        return f"number:{self.number}\nfirstname:{self.firstname}\nlastname:{self.lastname}\n" \
               f"age:{self.age}\n" \
               f"e-mail:{self.e_mail}\nskills:{self.skills}\npeople_lang:{self.people_lang}\n" \
               f"coding_lang:{self.coding_lang}"

    def create_file_json(self):
        with open('file_hw14.json', 'w') as file:
            json.dump([{self.number: {"firstname": self.firstname, "lastname": self.lastname, "age": self.age,
                                      "e-mail": self.e_mail, "skills": self.skills, "people_lang": self.people_lang,
                                      "coding_lang": self.coding_lang}}], file)

with open('file_hw14.json', 'r') as file:
    text = file.readline()
    dict = json.loads(text)
    list_with_keys = list(dict[0].keys())
    list_with_data = list(dict[0]["1"].values())
    list_objed = list_with_keys + list_with_data





emploee1 = Employee(1, "oleksii", "test", 22, "test@test.ocm", "all", ['UKR', "ENG"], ['Python', "C++", "lisp"])
emploee2 = Employee(2, "Dima", "Dimanich", 50, "ololo@test.ocm", "all", ['UKR', "ENG"], ['Python', "C++", "lisp"])
emploee3 = Employee(*list_objed)

print(emploee3)


