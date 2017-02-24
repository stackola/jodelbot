#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jodel_api
import sqlite3
import requests
import time
import json
import sys

conn = sqlite3.connect('db.db')
c = conn.cursor()
lat, lng, city = 51.05089, 13.73832, "Dresden"
# Fetch accounts from db
c.execute('SELECT * FROM accs')
acc = c.fetchone();

access_token=acc[0];
expiration_date=acc[1];
refresh_token=acc[2];
distinct_id=acc[3];
device_uid=acc[4];

#do work
j = jodel_api.JodelAccount(lat=lat, lng=lng, city=city, access_token=access_token, expiration_date=expiration_date, 
                               refresh_token=refresh_token, distinct_id=distinct_id, device_uid=device_uid)
##print j.get_account_data()
j.refresh_all_tokens()
j.verify_account()
#j = jodel_api.JodelAccount(lat=lat, lng=lng, city=city)
d = j.get_account_data()
c.execute("DELETE FROM accs")
c.execute("INSERT INTO accs VALUES ('"+str(d['access_token'])+"','"+str(d['expiration_date'])+"','"+str(d['refresh_token'])+"','"+str(d['distinct_id'])+"','"+str(d['device_uid'])+"')")
#j.refresh_all_tokens()
#print j.get_posts_recent(skip=None, limit=60, mine=False)
j.set_location(lat, lng, city, country=None, name=None) 
#print j.create_post("If you see this, my API works.", imgpath=None, color=None)

#c.execute('SELECT * FROM accs')
#print c.fetchone()
conn.commit()
conn.close()
#print j.get_posts_recent(skip=None, limit=60, mine=True)


#account is verified and ready.
#print j.create_post(message="Test-reply #3stundengewartet", imgpath=None, color=None, ancestor="58af6658d24832d276eea172")
exit
while (True):
	post= j.get_post_details("58af6658d24832d276eea172")
	post=post[1]
	print (post)



	sys.exit()

	# t = open("test.txt","w")
	# t.truncate()
	# t.write(json.dumps(post))
	# t.close()
	print "got post"
	for child in post["children"]:
		print "going through child"
		m= child["message"].encode("ascii", "ignore")
		print m
		if (m.find("Hashtag")!=-1):			
			print "match"


	time.sleep(5)



