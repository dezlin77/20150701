
file = open("text1.txt")
contents = file.read()
print(contents)
file.close()

OR
with open("text1.txt") as file:
  contents = file.read()
  print(contents)

with open("text1.txt", mode="a") as file:
  file.write("\nnew text.")
  


#https://brucefwebster.com/2013/09/13/the-real-software-crisis-byte-magazine-january-1996/

#https://brucefwebster.com/2008/01/10/the-wetware-crisis-tepes/

