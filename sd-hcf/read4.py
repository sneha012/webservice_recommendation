#Reading throughput and response time values from modified text and creating usd values

import re
import random

with open("tpUSD1.txt") as f1:
    text1 = f1.read()

sentences = re.split(r'[\n\r]+', text1)
final1 = []
for i in sentences:
	news = re.split(r'\t',i)
	news = news[:-1]
	final1.append(news)


with open("rtUSD1.txt") as f2:
    text2 = f2.read()

sentences = re.split(r'[\n\r]+', text1)
final2 = []
for i in sentences:
	news = re.split(r'\t',i)
	news = news[:-1]
	final2.append(news)


#->Now computed weighted average of USD values
#  to get customer rating for each service



for i in range(99):
	for j in range(500):
		output = (0.5*float(final1[i][j])) + (0.5*float(final2[i][j]))
		with open("ratings.txt","a") as fptr:
			fptr.write("%s\t" % (output))
		
	with open("ratings.txt","a") as fptr:
		fptr.write("\n")	