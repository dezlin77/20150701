
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
  
  
#CSV file
with open("weather_data.csv") as data_file:
  data = data_file.readlines()
  print(data)

#
import csv

with open("weather_data.csv") as data_file:
  data = csv.reader(data_file)
  for row in data:
    print(row)

#OR

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

print(data["temp"].mean())
  
#https://brucefwebster.com/2013/09/13/the-real-software-crisis-byte-magazine-january-1996/

#https://brucefwebster.com/2008/01/10/the-wetware-crisis-tepes/


