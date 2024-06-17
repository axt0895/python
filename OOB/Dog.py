class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.bark = 'barking'

    def description(self):
        print(f'{self.name} {self.breed} {self.age}')

    def make_sound(self):
        print(f'{self.name} is {self.bark}')




pepsi = Dog('Pepsi', 'Japanese Spitz', 14)
max = Dog('Max', 'Pomerian Husky', 12)
pepsi.description()
pepsi.make_sound()


max.description()
max.make_sound()