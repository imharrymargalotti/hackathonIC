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

    # create user if user id doesn't exist
    try:
        sql = "INSERT INTO Users (id, name) VALUES (%s, %s)"
        val = (info.get('author_id'), info.get('author'))
        cursor.execute(sql, val)
    except:
        print("User exists")

    # create subreddit if it doesn't already exist
    try:
        sql = "INSERT INTO SubReddits (id, name) VALUES (%s, %s)"
        val = (info.get('subreddit_id'), info.get('subreddit'))
        cursor.execute(sql, val)
    except:
        print("Subreddit exists")

    # insert post
    sql = "INSERT INTO Posts (id, title, date, link, sentiment, karma, user_id, subreddit_id, subject_id ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (info.get('post_id'), info.get('title'), info.get('date'), info.get('link'), info.get('sentiment'),
           info.get('karma'), info.get('author_id'), info.get('subreddit_id'), info.get('subject_id'))

    cursor.execute(sql, val)

    cnx.commit()

def insert_comment(info):
    # create sql query
    cursor = cnx.cursor()

    # create user if user id doesn't exist
    try:
        sql = "INSERT INTO Users (id, name) VALUES (%s, %s)"
        val = (info.get('author_id'), info.get('author'))
        cursor.execute(sql, val)
    except:
        print("User exists")

    # insert comment
    sql = "INSERT INTO Comments (id, body, date, link, karma, sentiment, user_id, post_id, subject_id, parent_id ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (info.get('comment_id'), info.get('bosy'), info.get('date'), info.get('permalink'), info.get('score'),
           info.get('sentiment'), info.get('author_id'), info.get('post_id'), info.get('subject_id'), info.get('parent_id'))

    cursor.execute(sql, val)

    cnx.commit()

