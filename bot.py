import jodel_api
import sqlite3
conn = sqlite3.connect('db.db')
c = conn.cursor()
lat, lng, city = 51.05089, 13.73832, "Dresden"
# Fetch accounts from db


#do work


#j = jodel_api.JodelAccount(lat=lat, lng=lng, city=city)
#d = j.get_account_data()
#c.execute("INSERT INTO accs VALUES ('"+str(d['access_token'])+"','"+str(d['expiration_date'])+"','"+str(d['refresh_token'])+"','"+str(d['distinct_id'])+"','"+str(d['device_uid'])+"')")
#j.refresh_all_tokens()
#print j.get_posts_recent(skip=None, limit=60, mine=False)
#j.set_location(lat, lng, city, country=None, name=None) 
#print j.create_post("If you see this, my API works.", imgpath=None, color=None)

#c.execute('SELECT * FROM accs')
#print c.fetchone()
#conn.commit();
#conn.close();