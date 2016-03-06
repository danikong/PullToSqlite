import sqlite3, time, datetime, random

class sql_handling():

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect('{0}.db'.format(self.db_name))
        self.c = self.conn.cursor()

        self.create_table()

    def create_s_table(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS tempSens_s(id INTEGER PRIMARY KEY AUTOINCREMENT, sens_id INTEGER, timestamp REAL, value REAL)")
        self.conn.commit()

#    def create_l_table(self):
#        self.c.execute("CREATE TABLE IF NOT EXISTS tempSens_s(id INTEGER PRIMARY KEY AUTOINCREMENT, day TEXT, sens_id INTEGER, value REAL)")

    def entry_tempsens_s(self, table_name, value):
        self.c.execute("INSERT INTO tempSens_s(sens_id, timestamp, value) VALUES (?, ?, ?)",
                       (id, time.time(), value))
        self.conn.commit()

    def readout_tempsens_s(self, table_name):
        self.c.execute("SELECT * FROM ?"(table_name))

    def close_db(self):
        self.c.close()
        self.conn.close()

#db_c = sql_handling("temperature")

for i in range(20):
    #db_c.entry_tempsens_s(random.randrange(0, 3),random.randrange(0, 30))
    hello = "hello world"
    time.sleep(0.5)


#db_c.close_db()