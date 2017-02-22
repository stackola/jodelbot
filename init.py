import sqlite3
conn = sqlite3.connect('db.db')
c = conn.cursor()
c.execute('''CREATE TABLE accs
            (token text, expiration text, refresh_token text, distinct_id text, device_uid text)''')
conn.commit()
conn.close()