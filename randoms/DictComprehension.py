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





