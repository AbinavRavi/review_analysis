from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# def get_sentiment(text):
#     """takes a preprocessed text and gives teh sentiment of the text

#     Args:
#         text (str): Input text

#     Returns:
#         sentiment_score, sentiment polarity: _description_
#     """
#     analyzer = SentimentIntensityAnalyzer()
#     sentiment_score = analyzer.polarity_scores(text)
#     if sentiment_score['neg'] > 0.5:
#         output = (sentiment_score['neg'], 'negative')
#     elif sentiment_score['pos'] > 0.5:
#         output = (sentiment_score['pos'], 'positive')
#     else:
#         output = (sentiment_score['neu'], 'neutral')
#     return output

# def extract_issue_text(text):
#     analyzer = SentimentIntensityAnalyzer()
#     sentiment_scores = analyzer.polarity_scores(text)
#     if sentiment_scores['compound'] < 0:
#         issues = [word for word in text.split() if analyzer.polarity_scores(word)['compound'] < 0]
#         issue_text = ', '.join(issues)
#     return issue_text

class SentimentAnalysis:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def get_sentiment(self, text):
        sentiment_score = self.analyzer.polarity_scores(text)
        sentiment = max(sentiment_score, key=sentiment_score.get)
        value = sentiment_score[sentiment]
        return sentiment, value
    
    def extract_issue_text(self,text):
        sentiment_scores = self.analyzer.polarity_scores(text)
        if sentiment_scores['compound'] < 0:
            issues = [word for word in text.split() if self.analyzer.polarity_scores(word)['compound'] < 0]
            issue_text = ', '.join(issues)
        return issue_text
