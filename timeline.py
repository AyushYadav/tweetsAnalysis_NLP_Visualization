#!/usr/bin/env python
import operator
import csv
f=open('tweet.csv','r')
data={}
for i in f:
	x=i.split('-`-')
	if(len(x)<4):
		continue
	else:
		d=x[3]
		if(d.endswith('2016 ')):
			da=d.split(':')
			da=da[0]
			l=da.split(' ')
			l1=l[2]+l[3]
			da=l1+'--'+da
			if(data.has_key(da)):
				data[da]+=1
			else:
				data[da]=1
sorted_x = sorted(data.items(), key=operator.itemgetter(0))

# Sun Jan 24 04:24:11 +0000 2016 


with open('out_vemula_unformat.csv','w') as out:
    csv_out=csv.writer(out)
    # csv_out.writerow(['date','tweets'])
    for row in sorted_x:
        csv_out.writerow(row)
# ['[\'' + row[0] +'\','+ str(row[1]) + '],']
fileid = open("out_vemula_unformat.csv","r")
f=open('tim.txt','w')
for i in fileid:
	i=i.split('--')
	i=i[1]
	i=i.split(',')
	f.write('[\''+i[0]+'\','+i[1]+'],')
f.close()
fileid.close()


# read = csv.reader(fileid)
# date = []
# count = []
# for row in reader:
# 	date.append(row[0])
# 	count.append(row[1])


