from abc import ABC, abstractmethod


class Shap(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shap):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius **2)

circle = Circle(10)
print(circle.area())
