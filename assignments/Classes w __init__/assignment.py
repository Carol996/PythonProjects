

#create a class, use __init__, an object, and method
class Pet:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age



Pet1 = Pet('Dog','Buck', 3)

print(Pet1.species)
print(Pet1.name)
print(Pet1.age)
    
