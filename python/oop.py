class Employee():
    """Created to capture essential Employee information"""
    def __init__(self, name, year_of_joining, salary):
        self.name = name
        self.year_of_joining = year_of_joining
        self.salary = salary

    def description(self):
        return f"{self.name} joined the firm on {self.year_of_joining}, and is currently paid {self.salary}."
    
class MixinDetails(Employee):
    Bonus = 0

    def distinction(self):
        if self.year_of_joining >= 2021:
            self.Bonus += 1
            return "Bonus increased by 1"

        elif 2005 <= self.year_of_joining <= 2011:
            self.Bonus += 2
            return "Bonus increased by 2"
        
        else:
            self.Bonus = 0
        return f"{self.name} is eligible for bonus."

            
class Projects(MixinDetails, Employee):
    """Contains project details"""
    def __init__(self, name, year_of_joining, salary, current_projects):
        self.current_projects= current_projects
        super().__init__(name, year_of_joining, salary)

    def description_2(self):
        return Employee.description(self) + f" {self.name} has worked on {self.current_projects}" 


my_variable = Projects("Narendran", 2022, 65000, ["Introduction to AI", "Introduction to the EU AI Act", "Risk Classification"])
print(my_variable.description())
print(my_variable.description_2())
print(my_variable.year_of_joining)
print(my_variable.distinction())
