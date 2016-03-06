import sqlite3, time, datetime, random

class sql_handling():

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect('{0}.db'.format(self.db_name))
        self.c = self.conn.cursor()

        #self.create_s_table()

    def create_s_table(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS tempSens_s(id INTEGER PRIMARY KEY AUTOINCREMENT, sens_id INTEGER, timestamp REAL, value REAL)")
        self.conn.commit()

    def entry_tempsens_s(self, table_name, sens_id, value):
        self.c.execute("INSERT INTO {0}(sens_id, timestamp, value) VALUES ({1}, {2}, {3})".format(table_name, sens_id, time.time(), value))
        self.conn.commit()

    def printout_tempsens_s(self, table_name):
        self.c.execute("SELECT * FROM {0}".format(table_name))
        data = self.c.fetchall()
        for row in data:
            print(row)

    def close_db(self):
        self.c.close()
        self.conn.close()

db_c = sql_handling("temperature")

#for i in range(20):
#    db_c.entry_tempsens_s("tempSens_s" , random.randrange(0, 3), random.randrange(0, 30))
#    time.sleep(0.5)

db_c.printout_tempsens_s("tempSens_s")
db_c.close_db()