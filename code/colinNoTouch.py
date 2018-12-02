import os
def main():
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
main()