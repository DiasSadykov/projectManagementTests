import re
import random

def find_between(s, start, end):
  return (s.split(start))[1].split(end)[0]

testnum = input("Enter test number: \n")
filename = 'tif_0'+testnum+'.doc'
data = open(filename, 'r', encoding="ISO-8859-1").read()
data = data.partition("Essay")[0]
data = data.partition("True False")[2]

d = {}
for x in range(1,30):
	q_num = str(x)+')'
	q_num_next = str(x+1)+')'
	question = find_between(data, q_num, 'Answer:')
	answer = find_between(data, 'Answer:  ' , q_num_next)
	d[question] = answer
	#print (question)
	#print (answer)

	data = data.partition(q_num_next)[1]+data.partition(q_num_next)[2]


data = data.partition("Multiple Choice")[2]


for x in range(1,45):
	q_num = str(x)+')'
	q_num_next = str(x+1)+')'
	question = find_between(data, q_num, 'Answer:')
	answer = find_between(data, 'Answer:  ' , q_num_next)
	d[question] = answer
	data = data.partition(q_num_next)[1]+data.partition(q_num_next)[2]
bank = []

choice = input("In order (1) / Random (2)\n")

if (choice == '2'):
	for q in d:
		question = random.choice(list(d))
		while True:
			if (question in bank):
				question = random.choice(list(d))
			else:
				bank.append(question)
				break
		print(question)
		ans = input("Your answer:\n")
		print (d[question])
elif(choice == '1'):
	for q in d:
		print (q)
		ans = input("Your answer:\n")
		print (d[q])
else:
	print("Choose correct option.")