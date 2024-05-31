#Dog --> sound --> "woof!"
#Cat --> sound --> "meow!"



class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

def make_sound(aniaml):
    print(aniaml.sound())

dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)