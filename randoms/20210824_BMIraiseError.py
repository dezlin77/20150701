


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
  raise ValueError("human height shouldn't be over 3 meters")

bmi = weight. height ** 2
print(bmi)


#new index error
fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
  try:
    fruit = fruits[index]
  except IndexError:
    print("Fruit pie")
  else:
    print(fruit + "pie")
    
make_pie(4)
