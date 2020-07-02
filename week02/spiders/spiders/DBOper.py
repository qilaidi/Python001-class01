import pymysql

import dbinfo

sqls = ['select 1', 'select version()']
result = []

class DBOper(object):
    def __init__(self):
        self.host = dbinfo.HOST
        self.port = dbinfo.PORT
        self.user = dbinfo.USERNAME
        self.password = dbinfo.PASSWORD
        self.db = dbinfo.DB

    def run(self):
        conn = pymysql.connect(self.host,
                               self.port,
                               self.user,
                               self.password,
                               self.db)
        cur = conn.cursor()
        try:
            for command in sqls:
                cur.execute(command)
                result.append(cur.fetchone())
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        conn.close()

if __name__ == "__main__":
    db = DBOper()
    db.run()
    print(result)
