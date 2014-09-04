import time
import os
import csv

class answer:
	answer_id=''
	question_id=''
	user_id=''
	date=''
	number_of_upvotes=''
	users_who_voted=''
	topics=''
	current_topic=''
	question_text=''
	answer_text=''
	def __init__(self, string):
		part = string.split("{{{")		
		self.answer_id = part[0].split(",")[0]
		self.question_id = part[0].split(",")[1]
		self.user_id = part[0].split(",")[2]
		self.date = part[0].split(",")[3]
		self.number_of_upvotes = part[0].split(",")[4]
		self.user_who_voted = part[1].split("}}}")[0]
		self.topics = part[2].split("}}}")[0]
		self.current_topic = part[2].split("}}}")[1].split(",")[1]
		self.question_text = part[3].split("}}}")[0]
		self.answer_text = part[4].split("}}}")[0]

f = open("answers.csv", "r")
a = csv.reader(f, delimiter=',')
answer_dict = {}
for row in a:
    line = ','.join(row)
    answer_dict[answer(line).answer_id] = answer(line)

f.close()
