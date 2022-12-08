from flask import render_template, redirect, url_for, flash, request

from core import app

import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS posts(
    id PRIMARY KEY,
    title TEXT,
    body TEXT
    )""")

conn.commit()


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/post_delete")
def post_delete():
    flash('Delete success', 'danger')
    return redirect(url_for('index'))


@app.route("/publish", methods=['GET', 'POST'])
def publish():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        cursor.execute('INSERT INTO posts (title, body) VALUES(:title, :body)', {'title': title, 'body' :body})
        conn.commit()
        flash('Publishied success', 'success')
        return redirect(url_for('index'))
    return render_template('publish.html')
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email == 'mercy@mail.ru' and password == 'mercy0119':
            return redirect(url_for('profile'))
        else:
            flash('Incorrect login or password', 'danger')    
    return render_template('login.html')

@app.route("/registration", methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        with open('registration.txt', 'a', encoding='utf-8') as f:
            f.write(email + '\n')
            f.write(password + '\n')
        flash('registrationied success', 'success')
        return redirect(url_for('index'))
    return render_template('registration.html')

@app.route('/logout')
def logout():
    flash('Logout success', 'success')
    return redirect(url_for('login'))
                    
@app.route("/add_comment", methods=['POST'])
def add_comment():
    message = request.form.get('message')
    with open('publish.txt', 'a', encoding='utf-8') as f:
        f.write(message + '\n')
    flash('Thx for comment', 'success')
    return redirect(url_for('post'))

@app.route('/profile')
def profile():
    if profile == None:
        flash('User ' + profile + ' not found.')
        return redirect(url_for('index'))
    return render_template('profile.html',
    nickname = profile)