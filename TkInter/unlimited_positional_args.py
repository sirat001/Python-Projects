def add(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
    
print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.coclor = kw.get("color")
        self.seats = kw.get('seat')

#in dictionary if we use the get method, if there is any missing arguments then it returns None instead of giving an error.

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)