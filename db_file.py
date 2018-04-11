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

# Авторизация


def entering(login, password):
    conn = getConnection()
    authorize_query = "SELECT emp_password FROM employees WHERE emp_login='%s'" % login
    cur1 = conn.cursor(MySQLdb.cursors.DictCursor)
    cur1.execute(authorize_query)
    data = cur1.fetchall()
    a = True
    if len(data) == 0:
        a = False
        return a
    else:
        password_bd = {}
        for item in data:
            password_bd = dict(item)
        if (password == password_bd['emp_password']):
            a = True
            return a
        else:
            a = False
            return a

# Проверка прав


def rights_check(login):
    conn = getConnection()
    right_query = "SELECT emp_rights FROM employees WHERE emp_login='%s'" % login
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute(right_query)
    right = curs.fetchall()
    for item in right:
        right_bd = dict(item)
        if (right_bd['emp_rights'] == 'min'):
            a = False
            return a
        elif (right_bd['emp_rights'] == 'max'):
            a = True
            return a
