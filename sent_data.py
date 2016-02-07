f=open('jonas_tweettext25.txt','r')
out=open('out_senti_jonas.txt','w')
for i in f:
	i=i.strip('\n')
	out.write('"'+i+'",')
f.close()
out.close()
