from sqlite3 import connect

conn = connect('db.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS user(
          User text,
          Rooms text
          )''')

c.execute('''CREATE TABLE IF NOT EXISTS rooms(
          Name text,
          Pwd text,
          Users text
          )''')

c.execute('''CREATE TABLE IF NOT EXISTS Msgs(
          room text,
          user text,
          msg text,
          time integer
          )''')

conn.commit()
