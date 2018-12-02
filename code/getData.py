import praw
import datetime
import os
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

reddit = praw.Reddit(client_id='KIjD0iw7Ppx4hA',
                     client_secret='8CI91ITeuvjHhHH15V1thu6yDdA',
                     user_agent='Get Data by /u/IthacaCompSci')

print("Connection read only to reddit: " + str(reddit.read_only))
print()

# assume you have a Reddit instance bound to variable `reddit`
subreddit = reddit.subreddit('politics')

print(subreddit.display_name)  # Output: redditdev

# empty list to add all comments into
post_comments = []
posts = []


# assume you have a Subreddit instance bound to variable `subreddit`
for submission in subreddit.hot(limit=1):
    # print(submission.subreddit_id[3:])  # Output: the subreddit id
    # print(submission.id)                # Output: the post id
    # print(submission.author)            # Output: the post author
    # print(submission.created_utc)       # Output: the creation timestamp
    # print(submission.title)             # Output: the submission's title
    # print(submission.score)             # Output: the submission's score
    # print(submission.upvote_ratio)      # Output: the submission's upvote/downvote ratio
    # print(submission.url)               # Output: the URL the submission points to
    #                                     # or the submission's URL if it's a self post
    post_info = {
        "subreddit_id" : submission.subreddit_id[3:],
        "subreddit": subreddit.display_name,
        "post_id" : submission.id,
        "author": submission.author,
        "author_id": reddit.redditor(str(submission.author)).id,
        "date": datetime.datetime.fromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
        "title": submission.title,
        "karma": submission.score,
        "vote_ratio": submission.upvote_ratio,
        "link": submission.url
    }
    print(post_info)
    posts.append(post_info)


    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        if comment.body != "[removed]":
            # pid = print("post id: " + str(comment.submission.id))
            # print("comment id: " + str(comment.id))
            # print("permalink: " + str(comment.permalink))
            # print("author: " + str(comment.author))
            # print("author id: " + str(reddit.redditor(str(comment.author)).id))
            # print("created time: " + str(comment.created_utc))
            # print("body: " + str(comment.body))
            # print("score: " + str(comment.score))
            # if str(comment.parent_id)[:2] != "t3":
            #     print("parent id: " + str(comment.parent_id)[3:])
            # else:
            #     print("parent id: null")
            # print()

            # get all info from comments and add to list
            info = {
                'post_id': comment.submission.id,
                'comment_id': comment.id,
                'permalink': comment.permalink,
                'author': comment.author,
                'author_id': reddit.redditor(str(comment.author)).id,
                'date': datetime.datetime.fromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
                'body': comment.body,
                'score': comment.score,
                'parent_id': (comment.parent_id if str(comment.parent_id)[:2] != "t3" else 'NULL')
            }
            post_comments.append(info)

    print(post_comments)

    print()

#this is harrys section do not write below this only above



os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = str('/Users/timc/Desktop/redditNLP-c250299d83e5.json')
# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = u'Hello, world!'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment

print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

for p in posts:
    text = p.get("title")
    document = types.Document(
        content = text,
        type = enums.Document.Type.PLAIN_TEXT
    )
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    p["sentiment"] = sentiment

for c in post_comments:
    text = c.get("body")
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT
    )
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    c["sentiment"] = sentiment


