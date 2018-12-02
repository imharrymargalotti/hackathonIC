'''
Created by Tim Clerico on Saturday December 1st
https://github.com/tclerico
'''

from neo4j.v1 import GraphDatabase
from mysqlstuff import *
import os
from environset import *

uri = "bolt://localhost:7687"
set_pass()
password = os.environ.get("PASSWORD")
driver = GraphDatabase.driver(uri, auth=("neo4j", password))


def create_nodes(tx):
    info = pull_all()

    # Users
    for usr in info.get("users"):
        tx.run("Create (:User {name: $name, id: $id})", name=usr[1], id=usr[0])

    # Create indices for user
    tx.run("Create INDEX ON :User(name)"
           "Create INDEX ON :User(id)")


    # Subreddits
    for sub in info.get("subreddits"):
        tx.run("Create (:SubReddit {name: $name, id: $id})", name=sub[1], id=sub[0])

    # Create indices for subreddits
    tx.run("Create INDEX ON :SubReddit(name)"
           "Create INDEX ON :SubReddit(id)")

    # Subjects
    # for s in info.get("subjects"):
    #     tx.run("Create (:Subject {name: $name, id: $id})", name=s[1], id=s[0])

    # Posts
    for p in info.get("posts"):
        tx.run("Create (:Post {title: $title, id: $id, date: $date, sentiment: $sentiment,"
               " karma: $karma, user_id: $uid, subreddit_id: $sub_id, subject_id: $subject_id",
               title=p[1], id=p[0], date=p[2], sentiment=p[4], karma=p[5], uid=p[6], sub_id=p[7], subject_id=p[8])

    # Create indices for Posts
    tx.run("Create index on :Post(id)"
           "Create index on :Post(date)"
           "Create index on :Post(sentiment)"
           "create index on :Post(user_id)"
           "create index on :Post(subreddit_id)")


    # Comments
    for c in info.get("comments"):
        tx.run("Create (:Comment {body: $body, id: $id, date: $date, karma: $karma, sentiment: $sentiment,"
               "user_id: $uid, post_id: $pid, subject_id: $sid, parent_id: $parent_id",
               body=c[1], id=c[0], date=c[2], karma=c[4], sentiment=c[5], uid=c[6], pid=c[7], sid=c[8], parent_id=c[9])

    # Create indices for Comments
    tx.run("Create index on :Comment(id)"
           "Create index on :Comment(date)"
           "Create index on :Comment(sentiment)"
           "create index on :Comment(user_id)"
           "create index on :Comment(post_id)")

with driver.session() as session:
    session.write_transaction()
