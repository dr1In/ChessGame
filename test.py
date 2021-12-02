class Car():
    def __init__(self, name: str()):
        self.name = name

class smallCar(Car):
    def get_name(self):
        print(self.name)

s = {'car': smallCar}

car = s['car']('audi')

car.get_name()