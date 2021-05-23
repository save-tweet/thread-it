from flask import render_template, url_for, redirect, send_file
from tspkg import app
from tspkg.models import User
from flask_login import logout_user, login_required
from flask_dance.contrib.twitter import twitter


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


#user = User.query.filter_by(user_id='user').first()  # dummy need to be cleared


@app.route("/dashboard")
def dashboard():
    if not twitter.authorized:
        return redirect(url_for("twitter.login"))
    resp = twitter.get("account/verify_credentials.json")
    assert resp.ok
    user_data = resp.json()
    user_id = user_data['id_str']
    user_name = user_data['screen_name']
    tweets = User.query.filter_by(user_id=user_id).all()
    # with open('ts_file.txt', 'w') as file:
    #     file.write(user.tweet)
    return render_template('dashboard.html', title='Dashboard', value=user_name, tweets=tweets)


@app.route("/download/<string:text>")
def download(text):
    with open('tweet.txt', 'w') as file:
        file.write(text)
    path = '../tweet.txt'
    return send_file(path, as_attachment=True)


@app.route('/downloadall')
def download_all():
    tweets = User.query.filter_by(user_id='user1').all()
    with open('tweet.txt', 'w') as file:
        for tweet in tweets:
            file.write(tweet.tweet)
            file.write('\n')
    path = '../tweet.txt'
    return send_file(path, as_attachment=True)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
