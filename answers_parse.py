import os

# main function

source_file = open("./answers_text.txt", mode = 'r')
#modeified_file = open("./answers_modeify.txt", mode = 'w')

counter = 0

for line in source_file:
	if line[0] != 'A':
		continue
	else:
		# remove "Answer:"
		line = line.split("Answer:")[1]
		
		# remove " can "
		num = line.count(" can ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" can ")[i]
			line = result
		# remove " will "
		num = line.count(" will ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" will ")[i]
			line = result
		# remove " the "
		num = line.count(" the ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" the ")[i]
			line = result
		# remove " The "
		num = line.count(" The ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" The ")[i]
			line = result
		# remove " one "
		num = line.count(" one ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" one ")[i]
			line = result
		# remove " just "
		num = line.count(" just ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" just ")[i]
			line = result
		# remove " also "
		num = line.count(" also ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" also ")[i]
			line = result
		# remove " much "
		num = line.count(" much ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" much ")[i]
			line = result
		# remove " many "
		num = line.count(" many ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" many ")[i]
			line = result
		# remove " even "
		num = line.count(" even ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" even ")[i]
			line = result
		# remove " this "
		num = line.count(" this ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" this ")[i]
			line = result
		# remove " This "
		num = line.count(" This ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" This ")[i]
			line = result
		# remove " dont "
		num = line.count(" dont ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" dont ")[i]
			line = result
		# remove " like "
		num = line.count(" like ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" like ")[i]
			line = result
		# remove " but "
		num = line.count(" but ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" but ")[i]
			line = result
		# remove " But "
		num = line.count(" But ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" But ")[i]
			line = result
		# remove " you "
		num = line.count(" you ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" you ")[i]
			line = result
		# remove " may "
		num = line.count(" may ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" may ")[i]
			line = result
		# remove " there "
		num = line.count(" there ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" there ")[i]
			line = result
		# remove " there, "
		num = line.count(" there, ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + ", " + line.split(" there, ")[i]
			line = result
		# remove " There "
		num = line.count(" There ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" There ")[i]
			line = result
		# remove " need "
		num = line.count(" need ")
		if num != 0:
			result = ""
			for i in range (0, num + 1):
				result = result + " " + line.split(" need ")[i]
			line = result


		len = 0
		for word in line.split(' '):
			len = len + 1


		if len > 5:	
			counter = counter + 1
			file = open('./Answers/Answer_' + str(counter) + '.txt', mode = 'w+')
			file.write(line)
			file.close()
			#modeified_file.write(line)
#modeified_file.close
source_file.close()
