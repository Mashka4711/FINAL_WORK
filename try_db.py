import MySQLdb

try:
    conn = MySQLdb.connect(host="localhost", user="root",
                           passwd="root", db="database_1", charset="utf8")
except MySQLdb.Error as err:
    print("Connection error: {}".format(err))
    conn.close()

test = 'Алиби'

sql = "SELECT * FROM guide"
test_query = "SELECT * FROM guide WHERE term_name='%s'" % test

try:
    cur = conn.cursor(MySQLdb.cursors.DictCursor)
    #cur.execute(sql)
    cur.execute(test_query)
    data = cur.fetchall()
except MySQLdb.Error as err:
    print("Query error: {}".format(err))

print(data)