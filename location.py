#!/usr/bin/env python

f=open('tweet.csv','r')
data={}
for i in f:
	x=i.split('-`-')		
	
	if(len(x)==6):
		d=x[5].strip()
		# print d
		if(len(d)>0):
			# print d
			if(data.has_key(d)):
				data[d]+=1
			else:
				data[d]=1
# print data
for loc in data:
	print '[\'',
	print loc,
	print '\',',
	print data[loc],
	print '],'


# Output via commandline to -- loc.txt


# print str(data)
# sorted_x = sorted(data.items(), key=operator.itemgetter(0))

#susan ferrara-`- NBC10 Philadelphia -`- 691943016316211200 -`-Tue Jan 26 11:17:25 +0000 2016 -`- delaware county,pa -`- Eastern Time (US & Canada)