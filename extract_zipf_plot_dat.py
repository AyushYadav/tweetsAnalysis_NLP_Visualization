f=open('zipf_master_data.csv','r')
fo=open('out_zipf.txt','w')
for i in f:
	x=i.split(',')
	fo.write('[\''+x[0]+'\','+x[-1]+'],')
f.close()
fo.close()
