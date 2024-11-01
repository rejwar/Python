class Dog:
    def speak(self):
       return "Woof"

class Cat:
    def speak(self):
        return "Meow"

class Duck:
    def speak(self):
        return "Quack"

def make_it_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
duck = Duck()

make_it_speak(dog)
make_it_speak(cat)
make_it_speak(duck)