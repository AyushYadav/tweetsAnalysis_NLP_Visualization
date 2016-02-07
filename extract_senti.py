import operator
import csv
f=open('senti_score_out_final_subhash.txt','r')
senti={}
for i in f:
	i=float(i)
	i=i*10
	i=int(i)
	i=i-5
	if(senti.has_key(i)):
		senti[i]+=1
	else:
		senti[i]=1
sorted_x = sorted(senti.items(), key=operator.itemgetter(0))
f.close()

with open('out_senti_unformat.csv','w') as out:
    csv_out=csv.writer(out)
    # csv_out.writerow(['date','tweets'])
    for row in sorted_x:
        csv_out.writerow(row)
# ['[\'' + row[0] +'\','+ str(row[1]) + '],']
# fileid = open("out_senti_unformat.csv","r")
# f=open('out_senti.csv','w')
# for i in fileid:

# 	i=i[0]
# 	i=i.split(',')
# 	f.write('[\''+i[0]+'\','+i[1]+'],')
# f.close()
# fileid.close()

