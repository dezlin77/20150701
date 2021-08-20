#*args is positional, tuple, refer to them by tuple position.
#if you want to refer to them by name, use **kwargs

def add(*args):
  sum = 0
  for n in args:
    sum += n
  return sum

#args is a tuple fyi
    
print(add(3, 5, 7, 11, 17))



