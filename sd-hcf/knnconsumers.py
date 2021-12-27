import csv
import random
from random import randrange
import numpy 
import math
import operator

def load_csv(filename):
	with open(filename,'r') as file:
		reader=csv.reader(file)
		dataset=list(reader)
		return dataset

def algorithm(dataset,k):
	for i in range(99):
		similarity=[]
		for j in range(99):
			similarity.append(dataset[i*99+j])
		similarity.sort(key=operator.itemgetter(2),reverse=True)
		#print similarity
		ksimilar=[]
		for x in range(k):
			ksimilar.append(similarity[x][1])
		with open("kusers.csv","a") as f4:
			f4.write("%s %s \n" % (i+1,",".join(ksimilar)))
		


def main():
	filename="usersim.csv"
	dataset=load_csv(filename)
	k=10
	algorithm(dataset,11)
	
main()