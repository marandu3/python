class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def annoying(self):
        print("i am not annoying")

class Cat(Mammal):
    def jumping(self):
        print("i jump higher")

dog1=Dog()
dog1.annoying()
dog1.walk()

cat1=Cat()
cat1.jumping()
cat1.walk()