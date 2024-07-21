class Car:
    def __init__(self, make, model, year, color) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def display_car(self) -> None:
        print(f'{self.make} {self.model} {self.year} {self.color}')

    def calculate_age(self, current_year) -> None:
        age = current_year - self.year
        print(f'The age of a vehicle is {age}')


bmw = Car('BMW', 'Series 3', 2019, 'Brown')
mercedes = Car('Mercedes', 'C class', 2022, 'Red Wine')

bmw.display_car()
bmw.calculate_age(2025)