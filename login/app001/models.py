from flask_mysqldb import MySQL
import MySQLdb.cursors

from app001.routes import app
import bcrypt

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'cluser'
app.config['MYSQL_PASSWORD'] = 'zmffnwj2020'
app.config['MYSQL_DB'] = 'pythonlogin'
app.config['MYSQL_PORT'] = 33906

# Intialize MySQL
mysql = MySQL(app)

class User():
#    def login_check(input_username, input_password):
#        # bcrypt hash transfer
#        input_password = input_password.encode('utf-8')
        # MySQL DB에 해당 계정 정보가 있는지 확인
#        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (input_username, input_password)
#        # 값이 유무 확인 결과값 account 변수로 넣기
#        account = cursor.fetchone()
#        return account


    def login_check(username, password):
        # MySQL DB에 해당 계정 정보가 있는지 확인
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
        # 값이 유무 확인 결과값 account 변수로 넣기
        account = cursor.fetchone()
        return account


    def get_information(id):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', id)
        account = cursor.fetchone()
        return account

    def update_fromip(fromip, id):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('UPDATE `pythonlogin`.`accounts` SET `fromip`=%s WHERE `id`=%s', (fromip, str(id)))
        mysql.connection.commit()

    def check_username_exist(username):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username, ))
        account = cursor.fetchone()
        return account

    def update_fromip(fromip, id):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('UPDATE `accounts` SET `fromip`=%s WHERE `id`=%s', (fromip, str(id)))
        mysql.connection.commit()


    def useradd(username, password, email):
        # bcrypt hash transfer
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("INSERT INTO `accounts` (`username`, `password`, `email`) VALUES (%s, %s, %s)", (username, password, email))
        mysql.connection.commit()

    def check_email_exist(email):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = %s', (email,))
        account = cursor.fetchone()
        return account

