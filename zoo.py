import random

class Person: #class - should be noun and singular
    animals = ["zebra", "monkey", "elephant", "bird"]
    acts = ["eating", "walking", "running", "sleeping", "drinking", "hiding", "playing"]
    feels = ["happy", "nervous", "angry", "peaceful", "threatens", "not satisfied", "cheerful"]
    ways = ["straight", "left", "right", "back"]

    def __init__(self, name): #contructor
        self.name = name

    def watch(self): #method - should be verb(action)
        print(self.name+" is watching the "+random.choice(self.animals)+" "+random.choice(self.acts))

    def feed(self): #self = ของตัวมันเอง ของ object นี้
        animal = random.choice(self.animals)
        print(self.name+" is feeding "+animal+" and the "+animal+" feels "+random.choice(self.feels))

    def lookingFor(self):
        print(self.name+" is looking for "+random.choice(self.animals))

    def walk(self):
        print(self.name+" go "+random.choice(self.ways))

p1 = Person("Mon") #object
p1.watch()
p1.feed()
p1.lookingFor()
p1.walk()