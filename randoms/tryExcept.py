
#try means to try this line of code
try:
  file =open("a_file.txt")
#except means if the try line of code didn't work, then do the line of code in the except
#except:
#  print("There's an error")
except:
  file = open("a_file.txt", "w")
#if there's no a_file, create one.



