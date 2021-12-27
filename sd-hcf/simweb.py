#Similarity computation between web services

import re
import random
import math

def average(values):
	lst = [float(x) for x in values]
	total = sum(lst)
	total = float(total) #as list stores it as string instead of float
	avg = total / len(values)
	return avg

def average2(values):
	#print values
	lst = [float(x) for x in values]
	total = 0.0
	cnt = 0.0
	for val in lst:
		if val != 0.0:
			total += val
			cnt += 1.0 
	avg = total / cnt
	return avg

web1 = 30
web2 = 430

with open("websratings.txt") as f1:
    text1 = f1.read()
values = re.split(r'[\n\r]+', text1)
webs = [] #contains the entire ratings as a list of list
for val in values:
	news = re.split(r'\t',val)
	news = news[:-1]
	webs.append(news) 


for j in range(len(webs)-1):
	for i in range(len(webs)-1):
		web1=j+1
		web2=i+1
		web1_qosAvg = average2(webs[web1-1])
		web2_qosAvg = average2(webs[web2-1])

		#This will convert the string values into float
		webs = [[ float(x) for x in row]  for row in webs]

		#Computing Similarity

		#-> Find list of indexes in web1 qos values 
		#   whose values are not 0.0

		idx = 0
		web1_qoslist = []
		for val in webs[web1-1]:
			if val != 0.0:
				web1_qoslist.append(idx)
			idx+=1

		#-> Find list of indexes in user2 qos values 
		#   whose values are not 0.0

		idx = 0
		web2_qoslist = []
		for val in webs[web2-1]:
			if val != 0.0:
				web2_qoslist.append(idx)
			idx+=1

		#To find common users between web services using intersection
		common_webI = list(set(web1_qoslist) & set(web2_qoslist))

		#Union of web services for weighted part
		common_webU = list(set(web1_qoslist) | set(web2_qoslist))


		sum_val1 = 0 #for numerator part
		sum_val2 = 0 #for denominator part,first value
		sum_val3 = 0 #for denominator part,second value
		for idx in common_webI:
			term1 = (webs[web1-1][idx] - web1_qosAvg)
			sum_val2 += pow(term1,2)
			
			term2 = (webs[web2-1][idx] - web2_qosAvg)
			sum_val3 += pow(term2,2)

			result = term1 * term2
			sum_val1 += result


		#Computing final value
		if web1!=102 or web2!=103:
			similarity = (sum_val1) / ( (math.sqrt(sum_val2)) * (math.sqrt(sum_val3)) )
			final_similarity = ( float(len(common_webI)) / float(len(common_webU)) ) * similarity		
			print web1,web2,final_similarity 
