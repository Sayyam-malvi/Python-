# class employee:
#     def __init__(self,name,salary,bond):
#         self.name = name 
#         self.salary = salary 
#         self.bond = bond 

#     def get_info(self):
#         return f"The name of employee is {self.name}. The salary is {self.salary}. The bond of this employee with this company is {self.bond}"

# e1 = employee("sayyam",30000,4)
# print(e1.get_info())

# Just to be more clear 

class Animal:
    def __init__(self, animal_type):
        self.animal_type = animal_type

    def get_voice(self):
        if self.animal_type == "dog":
            return "bow"
        elif self.animal_type == "cat":
            return "meow"
        elif self.animal_type == "parrot":
            return "squawk"
        else:
            return "Unknown animal"

e1 = Animal("dog")
print(e1.get_voice()) 
