import MySQLdb

try:
    conn = MySQLdb.connect(host="localhost", user="root",
                           passwd="root", db="database_1", charset="utf8")
except MySQLdb.Error as err:
    print("Connection error: {}".format(err))
    conn.close()


sql = "SELECT * FROM guide"

try:
    cur = conn.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql)
    data = cur.fetchall()
except MySQLdb.Error as err:
    print("Query error: {}".format(err))

print(data)