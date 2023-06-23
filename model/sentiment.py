from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentAnalysis:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def get_sentiment(self, text):
        sentiment_score = self.analyzer.polarity_scores(text)
        sentiment_score.pop('compound')
        sentiment = max(sentiment_score, key=sentiment_score.get)
        value = sentiment_score[sentiment]
        return sentiment, value
    
    def extract_issue_text(self,text):
        sentiment_scores = self.analyzer.polarity_scores(text)
        if sentiment_scores['compound'] < 0:
            issues = [word for word in text.split() if self.analyzer.polarity_scores(word)['compound'] < 0]
            return issues
        
    def extract_positive_text(self,text):
        sentiment_scores = self.analyzer.polarity_scores(text)
        if sentiment_scores['compound'] > 0:
            issues = [word for word in text.split() if self.analyzer.polarity_scores(word)['compound'] > 0]
            return issues
