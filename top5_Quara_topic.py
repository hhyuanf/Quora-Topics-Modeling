f = open('answers_text.txt')
question_set = set()
topic_dict = dict()
flag = False
index = 0
for line in f:
	if line[0] != 'Q' and line[0] != 'T' and line[0] != 'A':
		index = 0
	else:
		l = line.rstrip()
		if index == 0:
			if l in question_set:
				flag = False
			else:
				flag = True
				question_set.add(l)
		elif index == 1:
			if flag:
				if l not in topic_dict:
					topic_dict[l] = 1
				else:
					new_value = topic_dict[l] + 1
					topic_dict[l] = new_value
		index += 1
sorted_topic = sorted(topic_dict.iteritems(), key=lambda x:-x[1])[:5]
for x in sorted_topic:
	print x

