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
for submission in subreddit.hot(limit=10):
    print(submission.author)  # Output: the post author
    print(submission.title)  # Output: the submission's title
    print(submission.score)  # Output: the submission's score
    print(submission.url)    # Output: the URL the submission points to
                             # or the submission's URL if it's a self post

    top_level_comments = list(submission.comments)
    all_comments = submission.comments.list()
    print(all_comments)
    print("")

