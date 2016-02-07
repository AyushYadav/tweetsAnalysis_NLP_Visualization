#!/usr/bin/env python
import operator
import csv
f=open('master_data.txt','r')
words={}

for line in f:
	wo=line.split(' ')	
	for x in wo:
		if(x.startswith('http')):
			continue
		if(x.startswith('@')):
			continue
		if(x.endswith('..')):
			continue
		x=x.lower()
		if(x.startswith('#')):
			x=x[1:]
		if(x.endswith('/n')):
			x=x[:-2]
		if(x.endswith('.')):
			x=x[:-1]
		if(x in words):
			words[x]+=1
		else:
			words[x]=1
sorted_x = sorted(words.items(), key=operator.itemgetter(1))
with open('zipf_master_data.csv','w') as out:
    csv_out=csv.writer(out)
    for row in sorted_x:
        csv_out.writerow(row)
