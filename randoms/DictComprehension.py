#new_dict ={new_key: new_value for item in list}

names = ['Alex', 'Brad', 'Chelsea', 'Don', 'Edward', 'Fred']
import random
student_scores = {student:random.randint(1, 100) for student in names}

#check out which students passed the test, got over 60 points
#passed_students = { int(student) > 60 for student in student_scores}
passed_students = { student:score for (student, score) in student_scores.items() if score >=60}

#take each word in given sentence and calculate the number of letters in each word
sentence = "hi how are you how do you do?"
result = {word:len(word) for word in sentence.split()}
print(result)

#convert celcius to fahrenheit
weather_c = {
  "Monday": 12,
  "Tue": 17,
  "Wed": 18,
  "Thurs": 21,
  "Fri": 17,
}
weather_f = {day:(temp_c*9/5)+32 for (day, temp_c) in weather_c.items()}
print(result)

