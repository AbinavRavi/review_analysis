from utils.utils import read_config, read_text_file
from preprocess.preprocess import preprocess_text, separate_reviews
from model.ner import NamedEntityRecognition
from model.sentiment import SentimentAnalysis
from utils.plot import generate_wordcloud, generate_bar_plot
from collections import Counter

def extract_product_insights(text, model, entity="PRODUCT"):
    ner = NamedEntityRecognition(model, entity)
    for review in text:
        product_names = ner.extract_product_names(review)
    product_counter = Counter(product_names)
    generate_wordcloud(product_counter)
    generate_bar_plot(product_counter, "Products by number")
    return product_names, product_counter

def extract_product_sentiment(text):
    sentiment = SentimentAnalysis()
    sentiment_list = []
    for review in text:
        sentiment_product = {}
        nature, value = sentiment.get_sentiment(review)
        sentiment_product["review"] = review
        sentiment_product["sentiment"] = nature
        sentiment_product["value"] = value
        sentiment_list.append(sentiment_product)
    return sentiment_list
    
def extract_issue(reviews):
    sentiment = SentimentAnalysis()
    issues_list = []
    for review in reviews:
        issue_dict = {}
        issue_text = sentiment.extract_issue_text(review)
        issue_dict["review"] = review
        issue_dict["issue"] = issue_text
        issues_list.append(issue_dict)
    return issues_list


if __name__ == "__main__":
    config_path = "./config.yml"
    config = read_config(config_path)
    raw_data = read_text_file(config["data"]["file"])
    list_of_reviews = separate_reviews(raw_data)
    preprocessed_text =  preprocess_text(list_of_reviews)
    