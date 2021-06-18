# vim app001/routes.py

from flask import render_template, request, redirect, url_for, session
import re
from app001 import app
from app001.models import User
import bcrypt


app.secret_key = 'your secret key'

# http://host:5005/login/ - this will be the login page, we need to use both GET and POST requests
@app.route('/login/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    # username과 password에 입력값이 있을 경우
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # 쉬운 checking을 위해 변수에 값 넣기
        username = request.form['username']
        password = request.form['password']
        account = User.login_check(username, password)
        # 정상적으로 유저가 있으면 새로운 세션 만들고, 없으면 로그인 실패 문구 출력하며 index 리다이렉트
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            #return 'Logged in successfully!'
            fromip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
            User.update_fromip(fromip, account['id'])
            return redirect(url_for('home'))
        else:
            msg = '잘못된 username/password!'
            return render_template('login.html', msg='')
    if 'loggedin' in session:
        return redirect(url_for('home'))
    # Show the login form with message (if any)
    return render_template('login.html', msg='')





# http://host:5005/home - this will be the home page, only accessible for loggedin users
@app.route('/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))





# http://host:5005/logout - this will be the logout page
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))




   
# http://host:5005/profile - this will be the profile page, only accessible for loggedin users
@app.route('/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        account = User.get_information([session['id']])
        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))



# get client's ip test
@app.route('/ip', methods=['GET'])
def client_ip():
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)




# http://host:5005/register - this will be register page
@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = 'Creating User Page'
    # If already loggedin, redirect to home
    if 'loggedin' in session:
        return redirect(url_for('home'))
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        username_already_exist = User.check_username_exist(username)
        email_already_exist = User.check_email_exist(email)
        if username_already_exist:
            msg = '이름이 존재합니다'
        elif email_already_exist:
            msg = 'email이 존재합니다'
        else:
            User.useradd(username, password, email)
            msg = '유저 생성 완료'
            return redirect(url_for('login'))
    return render_template('register.html', msg=msg)






