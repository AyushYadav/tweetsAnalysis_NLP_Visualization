f=open('qq.rtf','r')
# out=open('out_rand.txt','w')
s=""
for i in f:
	i=i.rstrip('\n')
	print i,
# out.close()
# print "".join(str(i.strip('\n')) for i in f)
