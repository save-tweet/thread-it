from flask import render_template, url_for, redirect, send_file
from tspkg import app
from tspkg.models import User
from flask_login import logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


user = User.query.filter_by(user_id='user').first()  # dummy need to be cleared


@app.route("/dashboard")
# @login_required
def dashboard():
    with open('ts_file.txt', 'w') as file:
        file.write(user.tweet)
    return render_template('dashboard.html', title='Dashboard', value=user)  # value is temporary

@app.route("/download")
def download():
    path = '../ts_file.txt'
    return send_file(path, as_attachment=True)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
