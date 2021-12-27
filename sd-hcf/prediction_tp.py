from math import sqrt
import re
def standard_deviation(lst, population=True):
    """Calculates the standard deviation for a list of numbers."""
    num_items = len(lst)
    mean = sum(lst) / num_items
    differences = [x - mean for x in lst]
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)
    # Note: it would be better to return a value and then print it outside
    # the function, but this is just a quick way to print out the values along
    # the way.
    if population is True:
        #print('This is POPULATION standard deviation.')
        variance = ssd / num_items
    else:
        #print('This is SAMPLE standard deviation.')
        variance = ssd / (num_items - 1)
    sd = sqrt(variance)
    return sd
    # You could `return sd` here.
    #print('The mean of {} is {}.'.format(lst, mean))
    #print('The differences are {}.'.format(differences))
    #print('The sum of squared differences is {}.'.format(ssd))
    #print('The variance is {}.'.format(variance))
    #print('The standard deviation is {}.'.format(sd))
    #print('--------------------------')


with open("tpmodified.txt") as f1:
    text1 = f1.read()

values = re.split(r'[\n\r]+', text1)
final = [] #contains the entire ratings as a list of list
for val in values:
	news = re.split(r'\t',val)
	news = news[:-1]
	final.append(news)
with open("tpmodifiedweb.txt") as f2:
    text2 = f2.read()
values2 = re.split(r'[\n\r]+', text2)
webs = [] #contains the entire ratings as a list of list
for val in values2:
	news = re.split(r'\t',val)
	news = news[:-1]
	webs.append(news)
with open("ktpusers.csv") as f3:
    text3 = f3.read()

values = re.split(r'[\n\r]+', text3)
N1 = [] #contains the entire ratings as a list of list
for val in values:
	news = re.split(r',',val)
	news = news[:-1]
	N1.append(news)
with open("ktpservices.csv") as f4:
    text4 = f4.read()

values = re.split(r'[\n\r]+', text4)
N2 = [] #contains the entire ratings as a list of list
for val in values:
	news = re.split(r',',val)
	news = news[:-1]
	N2.append(news)
with open("tpsimusers.txt") as f5:
    text5 = f5.read()

values = re.split(r'[\n\r]+', text5)
uqsimdash = [] #contains the entire ratings as a list of list
for val in values:
	news = re.split(r' ',val)
	uqsimdash.append(news)
with open("tpsimweb.txt") as f6:
    text6 = f6.read()

values = re.split(r'[\n\r]+', text6)
iqsimdash = [] #contains the entire ratings as a list of list
for val in values:
	news = re.split(r' ',val)
	iqsimdash.append(news)
for i in range(len(final)):
	for j in range(len(final[i])):
		final[i][j] =float(final[i][j])
for i in range(len(webs)):
	for j in range(len(webs[i])):
		webs[i][j] =float(webs[i][j])
for i in range(len(uqsimdash)):
	for j in range(len(uqsimdash[i])):
		uqsimdash[i][j] =float(uqsimdash[i][j])
for i in range(len(iqsimdash)):
	for j in range(len(iqsimdash[i])):
		iqsimdash[i][j] =float(iqsimdash[i][j])
for i in range(len(N1)):
	for j in range(len(N1[i])):
		N1[i][j] =int(N1[i][j])
for i in range(len(N2)):
	for j in range(len(N2[i])):
		N2[i][j] =int(N2[i][j])

def avg(values):
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

def utopsum(c,i):
    topsum=0.0
    for cj in N1[c]:
    	cj=cj-1
        topsum=topsum+uqsimdash[c*99+cj][2]* ((final[cj][i]-avg(final[cj]))/standard_deviation(final[cj]))
    return topsum
def ubottomsum(c):
    bottomsum=0.0
    for cj in N1[c]:
    	cj=cj-1
        bottomsum=bottomsum+uqsimdash[c*99+cj][2]
    return bottomsum
def itopsum(s,i):
    topsum=0.0
    for sj in N2[s]:
    	sj=sj-1
    	print sj
    	print iqsimdash[s*500+sj][2]
    	print webs[sj][i]
    	print standard_deviation(webs[sj])
        topsum=topsum+iqsimdash[s*500+sj][2]* ((webs[sj][i]-avg(webs[sj]))/standard_deviation(webs[sj]))
    return topsum
def ibottomsum(s):
    bottomsum=0.0
    for sj in N2[s]:
    	sj=sj-1
        bottomsum=bottomsum+iqsimdash[s*500+sj][2]
    return bottomsum
    #add to a list qos[i][s] and return list
#assume c to be the consumer and s to be the webservice we are concerned with qos[c][s]

userp=final
itemp=final
for s in range(len(webs)-1):
	i=0
	for c in webs[s]: 
		itemp[i][s]= avg(webs[s]) + standard_deviation(webs[s])*(itopsum(s,i)/ibottomsum(s))
		i=i+1
for c in range(len(final)-1):
	i=0
	for s in final[c]:
		userp[c][i]= avg(final[c]) + standard_deviation(final[c])*(utopsum(c,i)/ubottomsum(c))
		i=i+1

predicted1=final
predicted2=final
for c in range(len(final)):
	i=0
	for s in final[c]: 
		print i,c
		print final[c][i]
		with open("final_predicted_tp_userp.txt","a") as f5:
			f5.write("%f " % (userp[c][i]))
		with open("final_predicted_tp_itemp.txt","a") as f6:
			f6.write("%f " % (itemp[c][i]))
		x1=0.8 *userp[c][i]
		y1=0.2* itemp[c][i]
		x2=0.2 *userp[c][i]
		y2=0.8* itemp[c][i]		
		predicted1[c][i]= x1+y1
		predicted2[c][i]=x2+y2
		with open("final_predicted_tp_all_u.txt","a") as f4:
			f4.write("%f " % (predicted1[c][i]))
		with open("final_predicted_tp_all_i.txt","a") as f7:
			f7.write("%f " % (predicted2[c][i]))
		i=i+1
	with open("final_predicted_tp_all_u.txt","a") as f4:
		f4.write("\n")
	with open("final_predicted_tp_all_i.txt","a") as f7:
		f7.write("\n")
	with open("final_predicted_tp_userp.txt","a") as f5:
		f5.write("\n")
	with open("final_predicted_tp_itemp.txt","a") as f6:
		f6.write("\n")

#print userp
#print itemp
#iqos[c][s]=cavg(s) + standard_deviation(std_s(s))*()
#
#
#s = [98, 127, 133, 147, 170, 197, 201, 211, 255]
#standard_deviation(s)
#standard_deviation(s, population=False)
