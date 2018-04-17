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
    if len(data) == 0:
        return False
    else:
        password_bd = {}
        for item in data:
            password_bd = dict(item)
        if password == password_bd['emp_password']:
            return True
        else:
            return False

# Проверка прав


def rights_check(login):
    conn = getConnection()
    right_query = "SELECT emp_rights FROM employees WHERE emp_login='%s'" % login
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute(right_query)
    right = curs.fetchall()
    for item in right:
        right_bd = dict(item)
        if right_bd['emp_rights'] == 'min':
            return False
        if right_bd['emp_rights'] == 'max':
            return True

# Проверка на уже существующий логин


def login_comparison(login_rw):
    conn = getConnection()
    login_query = "SELECT emp_login FROM employees"
    curs_login = conn.cursor(MySQLdb.cursors.DictCursor)
    curs_login.execute(login_query)
    login = curs_login.fetchall()
    for item in login:
        login_bd = dict(item)
        if login_rw == login_bd['emp_login']:
            return True

# Проверка на уже существующий пароль


def pass_comparison(pass_rw):
    conn = getConnection()
    pass_query = "SELECT emp_password FROM employees"
    curs_pass = conn.cursor(MySQLdb.cursors.DictCursor)
    curs_pass.execute(pass_query)
    password = curs_pass.fetchall()
    for item in password:
        pass_bd = dict(item)
        if pass_rw == pass_bd['emp_password']:
            return True

# Запись в базу нового сотрудника


def new_emp_note(name, surname, patr, age, post, education, right, login, password):
    conn = getConnection()
    note_query = "INSERT INTO employees (emp_surname, emp_name, emp_patronimyc, emp_post, emp_rights," \
                 "emp_age, emp_education, emp_login, emp_password) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s'," \
                 " '%s', '%s')" % (surname, name, patr, post, right, age, education, login, password)
    curs_note = conn.cursor(MySQLdb.cursors.DictCursor)
    curs_note.execute(note_query)
    conn.commit()