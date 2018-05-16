import MySQLdb


def getConnection():
    conn = MySQLdb.connect(host="localhost", user="root",
                           passwd="root", db="database_2", charset="utf8")
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
        # return False
        return -1
    else:
        password_bd = {}
        for item in data:
            password_bd = dict(item)
        if password == password_bd['emp_password']:
            # return True
            id_query = "SELECT id_emp FROM employees WHERE emp_login='%s'" % login
            cur2 = conn.cursor(MySQLdb.cursors.DictCursor)
            cur2.execute(id_query)
            id_emp_dict = cur2.fetchall()
            id_emp_db = {}
            for item in id_emp_dict:
                id_emp_db = dict(item)
            # print(id_emp_db['id_emp'])
            return id_emp_db['id_emp']
        else:
            # return False
            return -1

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


def new_emp_note(name, surname, patr, age, post, education, right, login, password, photo):
    conn = getConnection()
    note_query = "INSERT INTO employees (emp_surname, emp_name, emp_patronimyc, emp_post, emp_rights," \
                 "emp_age, emp_education, emp_login, emp_password, emp_photo) VALUES ('%s', '%s', '%s', '%s', '%s'," \
                 " '%s', '%s', '%s', '%s', '%s')" % (surname, name, patr, post, right, age, education, login,
                                                     password, photo)
    try:
        curs_note = conn.cursor(MySQLdb.cursors.DictCursor)
        curs_note.execute(note_query)
    except MySQLdb.IntegrityError as err:
        print("Error: {}".format(err))
    conn.commit()

# Редактирование записи сотрудника


def edit_emp_note(id, name, surname, patr, age, post, education, right, login, password, photo):
    conn = getConnection()
    note_query = "UPDATE employees SET emp_surname = '%s', emp_name = '%s', emp_patronimyc = '%s', emp_post = '%s', " \
                 "emp_rights = '%s', emp_age = '%s', emp_education = '%s', emp_login = '%s', emp_password = '%s', emp_photo = '%s' " \
                 "WHERE id_emp = '%s'" % (surname, name, patr, post, right, age, education, login, password, photo, id)
    print(note_query)
    try:
        curs_note = conn.cursor(MySQLdb.cursors.DictCursor)
        curs_note.execute(note_query)
    except MySQLdb.IntegrityError as err:
        print("Error: {}".format(err))
    conn.commit()

# Загрузка записей из базы - из таблицы сотрудников


def load_emp_notes():
    conn = getConnection()
    notes_query = "SELECT * FROM employees"
    curs_notes = conn.cursor(MySQLdb.cursors.DictCursor)
    curs_notes.execute(notes_query)
    notes = curs_notes.fetchall()
    entries = []
    for note in notes:
        str_id = note['id_emp']
        str_name = note['emp_surname'] + " " + note['emp_name'] + " " + note['emp_patronimyc']
        str_age = note['emp_age']
        str_education = note['emp_education']
        str_post = note['emp_post']
        str_rights = note['emp_rights']
        str_login = note['emp_login']
        str_pass = note['emp_password']
        str_photo = note['emp_photo']
        entries.append( [str_id, str_name, str_age, str_education, str_post, str_rights, str_login, str_pass, str_photo] )
    return entries

# Загрузка ОДНОЙ записи из базы - из таблицы сотрудников


def load_emp_note(note_id):
    conn = getConnection()
    notes_query = "SELECT * FROM employees WHERE id_emp = '%s'" % note_id
    curs_notes = conn.cursor(MySQLdb.cursors.DictCursor)
    curs_notes.execute(notes_query)
    notes = curs_notes.fetchall()
    entries = []
    for note in notes:
        # str_id = note['id_emp']
        str_name = note['emp_name']
        str_surname = note['emp_surname']
        str_patr = note['emp_patronimyc']
        str_age = note['emp_age']
        str_education = note['emp_education']
        str_post = note['emp_post']
        str_rights = note['emp_rights']
        str_login = note['emp_login']
        str_pass = note['emp_password']
        str_photo = note['emp_photo']
        # entries.append( [str_name, str_surname, str_patr, str_age, str_education, str_post, str_rights, str_login, str_pass, str_photo] )
        entries = [str_name, str_surname, str_patr, str_age, str_education, str_post, str_rights, str_login, str_pass, str_photo]
    return entries

# Удаление записи из таблицы сотрудников


def del_emp(id_employee):
    conn = getConnection()
    del_query = "DELETE FROM employees WHERE id_emp = '%s'" % id_employee
    curs_del = conn.cursor(MySQLdb.cursors.DictCursor)
    curs_del.execute(del_query)
    conn.commit()

# Загрузка справочника


def load_directory(word_part):
    conn = getConnection()
    notes_query = "SELECT term_name FROM guide WHERE term_name LIKE '" + word_part + "%'"
    curs_notes = conn.cursor(MySQLdb.cursors.DictCursor)
    curs_notes.execute(notes_query)
    notes = curs_notes.fetchall()
    words = []
    for note in notes:
        str_word = note['term_name']
        words.append(str_word)
    return words

# Загрузка описания для выбранного слова из справочника


def load_description(word):
    conn = getConnection()
    notes_query = "SELECT * FROM guide WHERE term_name = '" + word + "'"
    curs_notes = conn.cursor(MySQLdb.cursors.DictCursor)
    curs_notes.execute(notes_query)
    notes = curs_notes.fetchall()
    str_word = ""
    for note in notes:
        str_word = note['description']
    return str_word

# Запись параметров алкогольной экспертизы в базу


def save_alcohol_calculation(calc_date, sex, weight, alc_cont, amount, fullness, res_concentration, result,
                             dossier_no_dossier, employees_id_emp):
    conn = getConnection()
    note_query = "INSERT INTO expertise_calc (calc_date, sex, weight, alc_cont, amount, fullness, res_concentration, " \
                 "result, dossier_no_dossier, employees_id_emp) VALUES ('%s', '%s', '%s', '%s', '%s'," \
                 " '%s', '%s', '%s', '%s', '%s')" % (calc_date, sex, weight, alc_cont, amount, fullness,
                                                     res_concentration, result, dossier_no_dossier, employees_id_emp)
    try:
        curs_note = conn.cursor(MySQLdb.cursors.DictCursor)
        curs_note.execute(note_query)
    except MySQLdb.IntegrityError as err:
        print("Error: {}".format(err))
    conn.commit()

# Загрузка списка фамилий и номеров дел для любой эскпертизы


def load_dossier_to_alcohol_combobox():
    conn = getConnection()
    notes_query = "SELECT * FROM dossier"
    curs_notes = conn.cursor(MySQLdb.cursors.DictCursor)
    curs_notes.execute(notes_query)
    notes = curs_notes.fetchall()
    entries = []
    for note in notes:
        str_id = str(note['no_dossier'])
        str_name = note['m_name'] + " " + note['surname']
        entries.append(str_id + "# " + str_name)
    return entries

# Запись в базу нового дела


def new_dossier(man_name, man_surname, man_birthday):
    conn = getConnection()
    note_query = "INSERT INTO dossier (m_name, surname, birthday) VALUES ('%s', '%s', '%s')" % (man_name, man_surname,
                                                                                                man_birthday)
    try:
        curs_note = conn.cursor(MySQLdb.cursors.DictCursor)
        curs_note.execute(note_query)
    except MySQLdb.IntegrityError as err:
        print("Error: {}".format(err))
    conn.commit()

# Запись параметров экспертизы удара головой в базу


def save_dip_plane_calculation(calc_date, weight, height, rigidity, dossier_no_dossier, employees_id_emp, res_power,
                               result):
    conn = getConnection()
    note_query = "INSERT INTO dip_plane_calc (calc_date, weight, height, rigidity, res_power, result," \
                 " dossier_no_dossier, employees_id_emp) VALUES ('%s', '%s', '%s', '%s', '%s'," \
                 " '%s', '%s', '%s')" % (calc_date, weight, height, rigidity, res_power, result, dossier_no_dossier,
                                         employees_id_emp)
    try:
        curs_note = conn.cursor(MySQLdb.cursors.DictCursor)
        curs_note.execute(note_query)
    except MySQLdb.IntegrityError as err:
        print("Error: {}".format(err))
    conn.commit()

# Запись параметров экспертизы ИМТ в базу


def save_bmi_calculation(calc_date, weight, height, res_bmi, result, dossier_no_dossier, employees_id_emp):
    conn = getConnection()
    note_query = "INSERT INTO bmi_calc (calc_date, weight, height, res_bmi, result, dossier_no_dossier," \
                 "employees_id_emp) VALUES ('%s', '%s', '%s', '%s', '%s'," \
                 " '%s', '%s')" % (calc_date, weight, height, res_bmi, result, dossier_no_dossier, employees_id_emp)
    try:
        curs_note = conn.cursor(MySQLdb.cursors.DictCursor)
        curs_note.execute(note_query)
    except MySQLdb.IntegrityError as err:
        print("Error: {}".format(err))
    conn.commit()

# Запись параметров экспертизы определения массы тела в базу


def save_body_weight_determination(calc_date, height, thorax, leg, breech, sex, res_weight, dossier_no_dossier,
                                   employees_id_emp):
    conn = getConnection()
    note_query = "INSERT INTO weight_determination (calc_date, height, thorax, leg, breech, sex, res_weight," \
                 "dossier_no_dossier, employees_id_emp) VALUES ('%s', '%s', '%s', '%s', '%s'," \
                 " '%s', '%s', '%s', '%s')" % (calc_date, height, thorax, leg, breech, sex, res_weight,
                                               dossier_no_dossier, employees_id_emp)
    try:
        curs_note = conn.cursor(MySQLdb.cursors.DictCursor)
        curs_note.execute(note_query)
    except MySQLdb.IntegrityError as err:
        print("Error: {}".format(err))
    conn.commit()


# Запись параметров экспертизы определения времени выведения алкоголя в базу


def save_alcohol_excretion(calc_date, weight, amount, alc_cont, res_time, dossier_no_dossier, employees_id_emp):
    conn = getConnection()
    note_query = "INSERT INTO alcohol_excretion (calc_date, weight, amount, alc_cont, res_time, dossier_no_dossier," \
                 "employees_id_emp) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (calc_date, weight, amount,
                                                                                          alc_cont, res_time,
                                                                                          dossier_no_dossier,
                                                                                          employees_id_emp)
    try:
        curs_note = conn.cursor(MySQLdb.cursors.DictCursor)
        curs_note.execute(note_query)
    except MySQLdb.IntegrityError as err:
        print("Error: {}".format(err))
    conn.commit()

# Запись параметров экспертизы определения биологического возраста базу


def save_bio_age(calc_date, glomeruli, arteries, stroma, res_age, dossier_no_dossier, employees_id_emp):
    conn = getConnection()
    note_query = "INSERT INTO bio_age_kidneys (calc_date, glomeruli, arteries, stroma, res_age, dossier_no_dossier," \
                 "employees_id_emp) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (calc_date, glomeruli,
                                                                                          arteries, stroma, res_age,
                                                                                          dossier_no_dossier,
                                                                                          employees_id_emp)
    print(note_query)
    try:
        curs_note = conn.cursor(MySQLdb.cursors.DictCursor)
        curs_note.execute(note_query)
    except MySQLdb.IntegrityError as err:
        print("Error: {}".format(err))
    conn.commit()
