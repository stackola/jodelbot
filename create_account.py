import jodel_api
import sqlite3
conn = sqlite3.connect('db.db')
c = conn.cursor()

lat, lng, city = 51.05089, 13.73832, "Dresden"
j = jodel_api.JodelAccount(lat=lat, lng=lng, city=city)
d = j.get_account_data()
c.execute("INSERT INTO accs VALUES ('"+str(d['access_token'])+"','"+str(d['expiration_date'])+"','"+str(d['refresh_token'])+"','"+str(d['distinct_id'])+"','"+str(d['device_uid'])+"')")

conn.commit();
conn.close();