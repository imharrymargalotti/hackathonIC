import os


def set_pass():
    os.environ["PASSWORD"] = 'Blazer1992'


def set_path():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = str('/Users/hmargalotti/Desktop/redditNLP-c250299d83e5.json')


def set_praw():
    os.environ['CLIENT_ID'] = ""
    os.environ['CLIENT_SECRET'] = ""
