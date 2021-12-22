from flask import Flask, render_template, session, request, redirect
from flask_session import Session
from cs50 import SQL
from hashlib import sha256
app = Flask(__name__)
from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)
db = SQL("sqlite:///messages.db")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@app.route('/', methods=["POST", "GET"])
def index():
    
    try:
        id =  session['id']
        id = db.execute("SELECT id FROM users WHERE id = ?", fernet.decrypt(id).decode())
        if bool(id):
            return render_template('mainpage.html')
    except:
        return render_template("index.html")
@app.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method=="GET":
        return render_template('signup.html')
    username = request.form.get('username')
    if not bool(str(db.execute('SELECT * FROM users WHERE username = ?', username))):
        return "USERNAME ALREADY TAKEN"
    password = request.form.get('password')
    #password = sha256(request.form.get('password').encode('ascii'))
    birthdate = request.form.get('birthdate')
    db.execute("INSERT INTO users(username, password) VALUES (?, ?)", username, password)
    id = db.execute("SELECT id FROM users WHERE username=? AND password=?", username, password)
    id = str(id[0]['id'])
    print(id)
    id = fernet.encrypt(id.encode())
    session['id'] = id
    return id

@app.route('/login', methods=["POST"])
def login():
        username = request.form.get('username')
        password=request.form.get('password')
        #password = sha256(request.form.get('password').encode('ascii'))
        id = db.execute("SELECT id FROM users WHERE username=? AND password=?", username, password)
        id = str(id[0]['id'])
        if bool(id):
            id = fernet.encrypt(id.encode())
            session['id'] = id
            return id
        else:
            return 'Wrong username or password'

@app.route('/logout', methods=["POST"])
def logout():
    session['id'] = ''
    return redirect('/')