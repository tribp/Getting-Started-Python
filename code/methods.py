
class Person:
    adult_age = 18
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    """Normal method"""
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    def is_adult(self):
        return self.age >= self.adult_age

    @classmethod
    def from_string(cls, person_str):   # alternative constructor like from csv input field
        name, age = person_str.split(',')
        return cls(name, int(age))
    
    @classmethod            # access to class variable -> impact on the class itself    
    def set_adult_age(cls, new_age):
        cls.adult_age = new_age
        
    @staticmethod   # no access to self or cls -> works like regular function !
    def bark():
        return "Woof! Woof!"

# Example usage
p1 = Person("Alice", 20)
print(p1.greet())  # Normal method
print(f"Is Alice an adult? {p1.is_adult()}")
p2 = Person.from_string("Bob,25")  # Class method as alternative constructor
print(p2.greet())
print(Person.bark())  # Static method
print(f"Adult age is: {Person.adult_age}")
Person.set_adult_age(21)  # Change class variable using class method
print(f"New adult age is: {Person.adult_age}")
print(f"Is Alice an adult? {p1.is_adult()}")

    