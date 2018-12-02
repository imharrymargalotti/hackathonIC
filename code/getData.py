import praw

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')

print("Connection read only to reddit: " + str(reddit.read_only))
print()

# assume you have a Reddit instance bound to variable `reddit`
subreddit = reddit.subreddit('politics')

print(subreddit.display_name)  # Output: redditdev

# assume you have a Subreddit instance bound to variable `subreddit`
for submission in subreddit.hot(limit=1):
    print(submission.subreddit_id[3:])  # Output: the subreddit id
    print(submission.id)                # Output: the post id
    print(submission.author)            # Output: the post author
    print(submission.created_utc)       # Output: the creation timestamp
    print(submission.title)             # Output: the submission's title
    print(submission.score)             # Output: the submission's score
    print(submission.upvote_ratio)      # Output: the submission's upvote/downvote ratio
    print(submission.url)               # Output: the URL the submission points to
                                        # or the submission's URL if it's a self post

    print()

    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        if comment.body != "[removed]":
            print("post id: " + str(comment.submission.id))
            print("comment id: " + str(comment.id))
            print("permalink: " + str(comment.permalink))
            print("author: " + str(comment.author))
            print("author id: " + str(reddit.redditor(str(comment.author)).id))
            print("created time: " + str(comment.created_utc))
            print("body: " + str(comment.body))
            print("score: " + str(comment.score))
            if str(comment.parent_id)[:2] != "t3":
                print("parent id: " + str(comment.parent_id)[3:])
            else:
                print("parent id: null")
            print()

    print()

#this is harrys section do not write below this only above

import os
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = str('/Users/harrymargalotti/Desktop/redditNLP-c250299d83e5.json')
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
