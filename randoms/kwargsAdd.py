#many keyworded arguments

# How to use a **kwargs dictionary safely
class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)





def calculate (n, **kwargs):
  print(kwargs)
#  for key, value in kwargs.items():
#    print(key)
#    print(value)
  n += kwargs["add"]
  n *= kwargs["multiply"]
  print(n)

calculate(add=3, multiply=5)


