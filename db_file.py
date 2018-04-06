import MySQLdb

def getConnection():
    conn = MySQLdb.connect(host="localhost", user="root",
                           passwd="root", db="database_1", charset="utf8")
    return conn
'''try:
    conn = MySQLdb.connect(host="localhost", user="root",
                               passwd="root", db="database_1", charset="utf8")
except MySQLdb.Error as err:
    print("Connection error: {}".format(err))
    conn.close()'''





test = 'Алиби'

test_query = "SELECT * FROM guide WHERE term_name='%s'" % test

'''try:
    cur = conn.cursor(MySQLdb.cursors.DictCursor)
    cur1 = conn.cursor(MySQLdb.cursors.DictCursor)
    #cur.execute(test_query)
    #data = cur.fetchall()
except MySQLdb.Error as err:
    print("Query error: {}".format(err))'''

#print(data)


def entering(login, password):
    conn = getConnection()
    pass_query = "SELECT emp_password FROM employees WHERE emp_login='%s'" % login
    cur1 = conn.cursor(MySQLdb.cursors.DictCursor)
    cur1.execute(pass_query)
    data = cur1.fetchall()
    print(data)
    password_bd = {}
    for item in data:
        password_bd = dict(item)
        print(password_bd)
    #print(password_bd['emp_password'])
    print(password_bd['emp_password'])
    if (password==password_bd['emp_password']):
        print('YES')
        return True

    else:
        print('NO')
        return False


entering('ilya_egorov', '12345678')