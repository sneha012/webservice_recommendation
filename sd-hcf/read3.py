#Reading throughput values from modified text and creating usd values

import re
import random

with open("tpmodified.txt") as f1:
    text1 = f1.read()

sentences = re.split(r'[\n\r]+', text1)
final = []
for i in sentences:
	news = re.split(r'\t',i)
	news = news[:-1]
	final.append(news)


#print max(final)
max_val = 0
min_val = 300

for val in final[:-1]:
	for val_i in val:
		actual_val = float(val_i) 
		if( actual_val> max_val):
			max_val = actual_val

		if( actual_val!=-1 and actual_val< min_val ):
			min_val = actual_val
	


print max_val
print min_val

range_n = float(max_val)/10.0
print range_n

#->Now use if conditon to divide into 10 classes
#  and assign rand values according to each class

for i in range(99):
	for j in range(500):
		

		if float(final[i][j]) >0.0  and float(final[i][j]) <=19.634:
			#round the random number generated to three decimal placess
			new_val = round(random.uniform(0,0.1),3)
			with open("tpUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) >19.634 and float(final[i][j]) <=33.19:
			new_val = round(random.uniform(0.1, 0.2),3)
			with open("tpUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) >33.19 and float(final[i][j]) <=58.746:
			new_val = round(random.uniform(0.2, 0.3),3)
			with open("tpUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) >58.746 and float(final[i][j]) <=78.302:
			new_val = round(random.uniform(0.3, 0.4),3)
			with open("tpUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) >78.302 and float(final[i][j]) <=97.858:
			new_val = round(random.uniform(0.4, 0.5),3)
			with open("tpUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) >97.858 and float(final[i][j]) <=117.414:
			new_val = round(random.uniform(0.5, 0.6),3)
			with open("tpUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) >117.414 and float(final[i][j]) <=136.97:
			new_val = round(random.uniform(0.6, 0.7),3)
			with open("tpUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) >136.97 and float(final[i][j]) <=156.526:
			new_val = round(random.uniform(0.7, 0.8),3)
			with open("tpUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) >156.526 and float(final[i][j]) <=176.082:
			new_val = round(random.uniform(0.8, 0.9),3)
			with open("tpUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) >176.082:
			new_val = round(random.uniform(0.9, 1),3)
			with open("tpUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))

		elif float(final[i][j]) <0:
			print "hello"
			new_val = 0
			with open("tpUSD1.txt","a") as fptr:
				fptr.write("%s\t" % (new_val))


	with open("tpUSD1.txt","a") as fptr:
		fptr.write("\n")













