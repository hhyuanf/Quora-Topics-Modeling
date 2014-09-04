import time
import os
import csv

class user:
	user_id = ''
	number_of_topics= ''
	number_of_blogs= ''
	number_of_questions= ''
	number_of_answers= ''
	number_of_edits= ''
	followers= ''
	following= ''

	def __init__(self, string):
		part = string.split("{{{")		
		self.user_id = part[0].split(",")[0]
		self.number_of_topics = part[0].split(",")[1]
		self.number_of_blogs = part[0].split(",")[2]
		self.number_of_questions = part[0].split(",")[3]
		self.number_of_answers = part[0].split(",")[4]
		self.number_of_edits = part[0].split(",")[5]
		self.followers = part[1].split("}}}")[0]
		self.following = part[2].split("}}}")[0]

f = open("users.csv", "r")
a = csv.reader(f, delimiter=',')
user_dict = {}
for row in a:
    line = ','.join(row)
    user_dict[user(line).user_id] = user(line)
                    
f.close()
