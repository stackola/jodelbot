#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jodel_api
import sqlite3
import requests
import datetime
today = datetime.date.today()
wochentage=["Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"]
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
#j.set_location(lat, lng, city, country=None, name=None) 
#print j.create_post("Test Jodel - Please Ignore", imgpath=None, color=None)

#c.execute('SELECT * FROM accs')
#print c.fetchone()
conn.commit()
conn.close()


#account is verified and ready.
#get food!

food = requests.get("http://openmensa.org/api/v2/canteens/79/meals")

startJodel="####MENSAJODEL####\n"
wtag=int(today.strftime('%w'))
print wtag
startJodel+=wochentage[wtag]+" - "
startJodel+=today.strftime('%d.%m')+"\n";
print startJodel;

