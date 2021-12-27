#Similarity computation between users

import re
import random
import math

def average(values):
	#print values
	lst = [float(x) for x in values]
	total = sum(lst)
	total = float(total) #as list stores it as string instead of float
	avg = total / len(values)
	return avg

def average2(values):
	#print values
	lst = [float(x) for x in values]
	total = 0
	cnt = 0
	for val in lst:
		if val != 0.0:
			total += val
			cnt += 1 
	avg = total / cnt
	return avg

#Reading ratings file into a matrix
with open("ratings.txt") as f1:
    text1 = f1.read()

values = re.split(r'[\n\r]+', text1)
final = [] #contains the entire ratings as a list of list
for val in values:
	news = re.split(r'\t',val)
	news = news[:-1]
	final.append(news)

input_user=3
for j in range(len(final)-1):
	for i in range(len(final)-1):
		user1=j+1
		user2=i+1
		user1_qosAvg = average(final[user1-1])
		user2_qosAvg = average(final[user2-1])

		#Computing Similarity

		#-> Find list of indexes in user1 qos values 
		#   whose values are not 0.0

		idx = 0
		user1_qoslist = []
		for val in final[user1-1]:
			if float(val) != 0.0:
				user1_qoslist.append(idx)
			idx+=1

		#-> Find list of indexes in user2 qos values 
		#   whose values are not 0.0

		idx = 0
		user2_qoslist = []
		for val in final[user2-1]:
			if float(val) != 0.0:
				user2_qoslist.append(idx)
			idx+=1

		#To find common web services between users
		common_usersI = list(set(user1_qoslist) & set(user2_qoslist))

		#Union of users for weighted part
		common_usersU = list(set(user1_qoslist) | set(user2_qoslist))

		#This will convert the string values into float
		final = [[ float(x) for x in row]  for row in final]

		sum_val1 = 0 #for numerator part
		sum_val2 = 0 #for denominator part,first value
		sum_val3 = 0 #for denominator part,second value
		for idx in common_usersI:
			term1 = (final[user1-1][idx] - user1_qosAvg)
			sum_val2 += pow(term1,2)
			
			term2 = (final[user2-1][idx] - user2_qosAvg)
			sum_val3 += pow(term2,2)

			result = term1 * term2
			sum_val1 += result


		#Computing final value
		similarity = (sum_val1) / ( (math.sqrt(sum_val2)) * (math.sqrt(sum_val3)) )
		final_similarity = ( float(len(common_usersI)) / float(len(common_usersU)) ) * similarity
		print user1,user2,final_similarity 
