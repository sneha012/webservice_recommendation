#Reading response time values from modified text and creating usd values

import re
import random

with open("rtmodified.txt") as f1:
    text1 = f1.read()

sentences = re.split(r'[\n\r]+', text1)
final = []
for i in sentences:
	news = re.split(r'\t',i)
	news = news[:-1]
	final.append(news)


#print max(final)
max_val = 0
min_val = 100

for val in final[:-1]:
	for val_i in val:
		actual_val = float(val_i) 
		if( actual_val> max_val):
			max_val = actual_val

		if( actual_val!=-1 and actual_val< min_val ):
			min_val = actual_val
	

print max_val
print min_val

range_n = float(max_val-min_val)/10.0
print range_n

#->Now use if conditon to divide into 10 classes
#  and assign rand values according to each class

for i in range(99):
	for j in range(500):
		
		if float(final[i][j]) >0.0  and float(final[i][j]) <=1.0: 
			#round the random number generated to three decimal placess
			new_val = round(random.uniform(0.9, 1),3)
			with open("rtUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) >1.0 and float(final[i][j]) <=2.0:
			new_val = round(random.uniform(0.8, 0.9),3)
			with open("rtUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) >2 and float(final[i][j]) <=3:
			new_val = round(random.uniform(0.7, 0.8),3)
			with open("rtUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) >3 and float(final[i][j]) <=4:
			new_val = round(random.uniform(0.6, 0.7),3)
			with open("rtUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) >4 and float(final[i][j]) <=5:
			new_val = round(random.uniform(0.5, 0.6),3)
			with open("rtUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) >5 and float(final[i][j]) <=6:
			new_val = round(random.uniform(0.4, 0.5),3)
			with open("rtUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) >6 and float(final[i][j]) <=7:
			new_val = round(random.uniform(0.3, 0.4),3)
			with open("rtUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) >7 and float(final[i][j]) <=8:
			new_val = round(random.uniform(0.2, 0.3),3)
			with open("rtUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) >8 and float(final[i][j]) <=9:
			new_val = round(random.uniform(0.1, 0.2),3)
			with open("rtUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) >9:
			new_val = round(random.uniform(0, 0.1),3)
			with open("rtUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) <0:
			print "hello"
			new_val = 0
			with open("rtUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))




	with open("rtUSD1.txt","a") as fptr:
		fptr.write("\n")













