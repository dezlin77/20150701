


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
  raise ValueError("human height shouldn't be over 3 meters")

bmi = weight. height ** 2
print(bmi)

