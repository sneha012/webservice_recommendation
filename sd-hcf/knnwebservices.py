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
		dataset_split=list()
		for i in dataset:
			dataset_split.append(i[0].split())
        #print dataset_split
	return dataset_split



def algorithm(dataset,k):
	for i in range(499):
		similarity=list()
		for j in range(499):
	 		similarity.append(dataset[i*499+j])
		#print similarity
		similarity.sort(key=operator.itemgetter(2),reverse=True)
		#print similarity
		#print similarity[0][1]
		ksimilar=list()
		for x in range(k):
			#print x
			ksimilar.append(similarity[x][1])
		for x in range(k):
			if ksimilar[x]<=0:
				ksimilar.remove(x);
		#print ksimilar
		with open("kwebservices.csv","a") as f4:
			f4.write("%s %s \n" % (i+1,",".join(ksimilar)))
		


def main():
	filename="webservicessim.csv"
	dataset=load_csv(filename)
	k=10
	algorithm(dataset,51)
	
main()
