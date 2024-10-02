class Person:
    def __init__(self, name, age, address) -> None:
        self.name = name
        self.age = age
        self.address = address
    
    def __str__(self) -> str:
        return f'My name is {self.name} aged {self.age} and I live in {self.address}'
    


anil = Person('Anil Thapa', 24, '1907 Sabine Pass Ln, 76006, Arlington')
anish = Person('Anil Thapa', 45, '801 Warhawk Way, Apt 20')

print(anil.name +' '+anil.address)
print(anish)