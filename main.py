from utils.utils import read_config, read_text_file
from preprocess.preprocess import preprocess_text, separate_reviews
from model.ner import NamedEntityRecognition
from model.sentiment import SentimentAnalysis
from utils.plot import generate_wordcloud, generate_bar_plot
from collections import Counter
from tqdm import tqdm
import matplotlib.pyplot as plt

def preprocess_review_data(text):
    processed_data = []
    for review in tqdm(text, desc="preprocessing"):
        processed_data.append(preprocess_text(review))
    return processed_data


def extract_product_insights(text, model, entity="PRODUCT"):
    ner = NamedEntityRecognition(model, entity)
    product_names = []
    for review in tqdm(text, desc="product_insights"):
        product_names.extend(ner.extract_product_names(review))
    product_counter = Counter(product_names)
    generate_wordcloud(product_counter,"products_wordcloud")
    plt.figure()
    generate_bar_plot(product_counter, "Products by number")
    return product_names, product_counter


def extract_product_sentiment(text):
    sentiment = SentimentAnalysis()
    sentiment_list = []
    for review in tqdm(text,"product_sentiment"):
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
    issue_words = []
    for review in tqdm(reviews, desc="issue_extractor"):
        issue_dict = {}
        issue_text = sentiment.extract_issue_text(review)
        issue_dict["review"] = review
        issue_dict["issue"] = issue_text
        issues_list.append(issue_dict)
        if issue_text == None:
            pass
        else:
            issue_words.extend(issue_text)
    word_counter = Counter(issue_words)
    # word_counter.pop(None)
    generate_wordcloud(word_counter, "issue_wordcloud")
    return issues_list

def extract_positives(reviews):
    sentiment = SentimentAnalysis()
    plus_list = []
    positives = []
    for review in tqdm(reviews, desc="positive_extractor"):
        plus_dict = {}
        plus_text = sentiment.extract_positive_text(review)
        plus_dict["review"] = review
        plus_dict["plus"] = plus_text
        plus_list.append(plus_dict)
        if plus_text == None:
            pass
        else:
            positives.extend(plus_text)
        positives.extend(plus_text)
    word_counter = Counter(positives)
    # print(word_counter)
    generate_wordcloud(word_counter, "positives_wordcloud")
    return plus_list

def extract_negative_reviews(sentiment_list):
    negative_reviews = []
    for item in tqdm(sentiment_list,desc="extract_negative_review"):
        if item["sentiment"] == "neg":
            negative_reviews.append(item["review"])
    # print(negative_reviews)
    return negative_reviews

def extract_positive_reviews(sentiment_list):
    positive_reviews = []
    for item in tqdm(sentiment_list,desc="extract_positive_review"):
        if item["sentiment"] == "pos":
            positive_reviews.append(item["review"])
    return positive_reviews


if __name__ == "__main__":
    config_path = "./config.yml"
    config = read_config(config_path)
    raw_data = read_text_file(config["data"]["file"])
    list_of_reviews, number_of_reviews = separate_reviews(raw_data)
    preprocessed_text =  preprocess_review_data(list_of_reviews)
    product_names, product_counter = extract_product_insights(preprocessed_text, config["model"]["english_model"])
    sentiment_list = extract_product_sentiment(preprocessed_text)
    negative_reviews = extract_negative_reviews(sentiment_list)
    issues_list = extract_issue(negative_reviews)
    positive_reviews = extract_positive_reviews(sentiment_list)
    positive_list = extract_positives(positive_reviews)
    



