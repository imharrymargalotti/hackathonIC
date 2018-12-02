'''
Created by Tim Clerico on Saturday December 1st
https://github.com/tclerico
'''

import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user="reddit@redditcodeathon", password='C0meF0rTheCats', host='redditcodeathon.mysql.database.azure.com', database='reddit', ssl_ca='/Users/timc/Desktop/redditrush.pem', ssl_verify_cert=True)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Auth Error")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("database doesn't exist")
    else:
        print(err)


def insert_post(info):
    # create sql query
    cursor = cnx.cursor()
    for i in info:
        # create user if user id doesn't exist
        try:
            sql = "INSERT INTO Users (id, name) VALUES (%s, %s)"
            val = (i.get('author_id'), i.get('author'))
            cursor.execute(sql, val)
        except:
            continue

        # create subreddit if it doesn't already exist
        try:
            sql = "INSERT INTO SubReddits (id, name) VALUES (%s, %s)"
            val = (i.get('subreddit_id'), i.get('subreddit'))
            cursor.execute(sql, val)
        except:
            print("Subreddit already exists")

        try:
            # insert post
            sql = "INSERT INTO Posts (id, title, date, link, sentiment, karma, user_id, subreddit_id, subject_id ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (i.get('post_id'), i.get('title'), i.get('date'), i.get('link'), i.get('sentiment'),
                   i.get('karma'), i.get('author_id'), i.get('subreddit_id'), 1)
            cursor.execute(sql, val)
        except:
            print("Post already exists")

    cnx.commit()


def insert_comment(info):
    # create sql query
    cursor = cnx.cursor()
    for i in info:
        # create user if user id doesn't exist
        try:
            sql = "INSERT INTO Users (id, name) VALUES (%s, %s)"
            val = (i.get('author_id'), i.get('author'))
            cursor.execute(sql, val)
        except:
            continue

        # insert comment
        sql = "INSERT INTO Comments (id, body, date, link, karma, sentiment, user_id, post_id, subject_id, parent_id ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (i.get('comment_id'), i.get('body'), i.get('date'), i.get('permalink'), i.get('score'),
               i.get('sentiment'), i.get('author_id'), i.get('post_id'), 1, i.get('parent_id'))
        cursor.execute(sql, val)

    'eavwie8'

    cnx.commit()


def pull_all():

    cursor = cnx.cursor()

    users = "SELECT * FROM Users"
    subreddits = "SELECT * FROM SubReddits"
    # subjects = "SELECT * FROM Subjects"
    posts = "SELECT * FROM Posts"
    comments = "SELECT * FROM Comments"
    # subreddit_sentiment = "SELECT * FROM subrsentiment"
    # usersentiment = "SELECT * FROM usersentiment"

    pull = dict()

    cursor.execute(users)
    pull["users"] = cursor.fetchall()
    cursor.execute(subreddits)
    pull["subreddits"] = cursor.fetchall()
    # cursor.execute(subjects)
    # pull["subjects"] = cursor.fetchall()
    cursor.execute(posts)
    pull["posts"] = cursor.fetchall()
    cursor.execute(comments)
    pull["comments"] = cursor.fetchall()
    # cursor.execute(subreddit_sentiment)
    # pull["subreddit_sentiment"] = cursor.fetchall()
    # cursor.execute(usersentiment)
    # pull["user_sentiment"] = cursor.fetchall()

    return pull




