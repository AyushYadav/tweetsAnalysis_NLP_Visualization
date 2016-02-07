#!/usr/bin/env python
import twitter
#Setting up Twitter API
api = twitter.Api(
 consumer_key='9N0JugZ0HOyB1tPoceJ8oVvmb',
 consumer_secret='20iW0ERGjrVei9HsxYcrFtfHdFaFHHLomfphwHiGuJoq4BDn1S',
 access_token_key='134418439-ORGHRwzlALoW4tFjXEWBXIAPpAs8RzbY96I11tII',
 access_token_secret='oprhHQMF4teld1PqagELxNozx8svXhLxTPbOwnV3Qa9dd' )

query='India Australia Cricket'
cnt=0;


# Output also via commandline to ----tweet.csv


f=open('tweettext.txt','w')
# fcs=open('arunachal_25.csv','w')
search = api.GetSearch(term=query,lang='en', count=100,max_id='')
#print search
for t in search:
	print t.user.name.encode('utf-8')+'-`-',
	if (t.retweeted_status):
		print t.retweeted_status.user.name.encode('utf-8'),
		print '-`-',
	else:
		print '-`-', 
	print t.id,
	print '-`-' + t.created_at.encode('utf-8'),
	print '-`-',
	if(t.user.location):
		print t.user.location.encode('utf-8'), 
	print '-`-',
	if(t.user.time_zone):
		print t.user.time_zone.encode('utf-8')
	else:
		print
	ff=t.text[:2]
	if(ff=='RT'):
		continue
	else:			
		f.write(t.text.encode('utf-8')+"\n")
		
				

max_id=t.id-1
while(max_id and cnt!=140):
	search = api.GetSearch(term=query, lang='en', count=100 ,max_id=max_id)
	#print search
	for t in search:
		print t.user.name.encode('utf-8')+'-`-',
		if (t.retweeted_status):
			print t.retweeted_status.user.name.encode('utf-8'),
			print '-`-',
		else:
			print '-`-', 
		print t.id,
		print '-`-' + t.created_at.encode('utf-8'),
		print '-`-',
		if(t.user.location):
			print t.user.location.encode('utf-8'), 
		print '-`-',
		if(t.user.time_zone):
			print t.user.time_zone.encode('utf-8')
		else:
			print
		ff=t.text[:2]
		if(ff=='RT'):
			continue
		else:
			f.write(t.text.encode('utf-8')+"\n")
	
		

	max_id=t.id-1
	cnt+=1

f.close()
