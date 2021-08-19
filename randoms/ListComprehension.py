
#square numbers using list comprehension
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n*n for n in numbers]

print(squared_numbers)

#filter even numbers

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

even_numbers = [n for n in numbers if n % 2 == 0]

print(even_numbers)

#compare two docs, and combine numbers common in both files

with open("file1.txt") as file1:
  file_1_data = file1.readlines()
  
with open("file2.txt") as file2:
  file_2_data = file2.readlines()
  
result = [int(num) for num in file_1_data if num in file_2_data]

print(result)
