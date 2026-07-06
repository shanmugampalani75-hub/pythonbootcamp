#Basic class definition
class Person:

    #Class attribute (shared by all instances)
    species = "Human"

    #Constructor method
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #instance method
    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."
    
    #Method with parameters
    def have_birthday(self):
        self.age += 1
        return f"Happy birthday! You are now {self.age} years old."

    
#Objects:
#creating obejcts (instances)
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

#Accessing attributes
print(person1.name)
print(person1.age)

#calling methods
print(person1.introduce())
print(person2.have_birthday())

#class attributes
print(Person.species)
print(person2.species)