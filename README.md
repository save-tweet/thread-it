![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)
# Project Name
A simple Twitter bot and a webpage which allows users to save any desired tweet or thread for later use just by mentioning this bot. The saved tweet/thread can be viewed in the webpage after loggin in with twitter. Users can also download tweets from webpage as a text file. They will also receive a copy of direct message from the bot.
## Team members
1. Alwin Joseph [https://github.com/alwin48]
2. Muhammed Rizal K E [https://github.com/MUHAMMEDRIZALKE]
3. Sankar Vinayak E P [https://github.com/sankarvinayak]
## Team Id
BFH/recbY0A1OBTpNxJ5c/2021
## Link to product walkthrough
[link to video]
## How it Works ?
### Bot
1. This project uses tweepy which is a Python library for accessing the Twitter API.
2. We use tweepy to get the mentions for our bot.
3. And using that mention, the thread/tweet is saved to a string along with the user who mentioned the bot.
4. The saved variables are pushed to an SQL database using sqlalchemy library.
5. The bot also sends a DM to the user with the thread
### Website
1. The website uses flask.
2. The website has a twitter login through which we get an userid of Twitter user.
3. Then the website searches for the userid in database and displays the result which can be downloaded as a thread.
## Libraries used
1. click==7.1.2
2. Flask==2.0.1
3. Flask-Dance==5.0.0
4. Flask-Login==0.5.0
5. Flask-SQLAlchemy==2.5.1
6. gunicorn==20.1.0
7. itsdangerous==2.0.1
8. Jinja2==3.0.1
9. SQLAlchemy==1.4.15
10. tweepy==3.10.0
11. psycopg2-binary==2.8.6
## How to configure
1. Clone the GitHub repository.
  ``` 
  git clone https://github.com/save-tweet/thread-it.git
  ```
2. Create a virtual environment and activate it using:
  ``` 
  virtualenv venv
  source venv/bin/activate
  ```
3. Install the libraries mentioned in requirements using:
  ``` 
  pip install <library>
  ```
## How to Run
Create 2 terminal instances. On first one run:
```
python main.py
```
And on second instance run
```
python wsgi.py
```
