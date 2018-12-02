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