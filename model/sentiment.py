from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_sentiment(text):
    """takes a preprocessed text and gives teh sentiment of the text

    Args:
        text (str): Input text

    Returns:
        sentiment_score, sentiment polarity: _description_
    """
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(text)
    if sentiment_score['neg'] > 0.5:
        output = (sentiment_score['neg'], 'negative')
    elif sentiment_score['pos'] > 0.5:
        output = (sentiment_score['pos'], 'positive')
    else:
        output = (sentiment_score['neu'], 'neutral')
    return output
