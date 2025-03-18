class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def move(self):
        print("move")
    
    def draw(self):
        print("draw")


point1 = Point(10,20)
print(point1.x)


class Person:
    def __init__(self,name):
        self.name=name
    
    def talk(self):
        print(f'hi there i am {self.name}')

john=Person("john")
john.talk()

bob=Person("bob smith")
bob.talk()
