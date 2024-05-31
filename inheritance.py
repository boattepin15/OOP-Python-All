#Vehicle
#Car

class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand) #ดึงคุณสมบัติของ Class Vehicle
        self.model = model

car = Car("Toyota", "X321")
print(car.brand)
print(car.model)




