from flask import Flask, request, render_template, url_for, get_template_attribute, flash, redirect, render_template, request, session, abort
from . import server_utilities as server


app = Flask(__name__, template_folder="./templates")


@app.route('/')
def home():
    if not server.logged_in(request.remote_addr):
        return render_template('login.html')
    else:
        return render_template('user_board.html',
                               username=server.get_username_by_addr(request.remote_addr),
                               messages=server.get_messages_by_addr(request.remote_addr))

@app.route('/login', methods=['POST'])
def login():
    POST_PUBLIC = str(request.form['public_key'])
    POST_PRIVATE = str(request.form['private_key'])
    server.login(request.remote_addr, POST_PUBLIC, POST_PRIVATE)
    return home()

@app.route("/logout")
def logout():
    server.logout(request.remote_addr)
    return home()

@app.route('/message', methods=['POST'])
def read_message():
    message = str(request.form['message'])
    server.save_message(request.remote_addr, message)
    return home()

@app.route('/find_user', methods=['POST'])
def find_user():
    user_name = str(request.form['user_name'])
    if server.find_user(request.remote_addr, user_name):
        return render_template('user_board.html',
                               username=user_name,
                               messages=server.get_messages_by_username(user_name))
    return home()

@app.route('/upload_file', methods=['POST'])
def upload_file():
    f = request.files['file']
    f.save(f.filename)
    print(f.filename)
    print(f)
    return home()


