import matplotlib.pyplot as plt
from wordcloud import WordCloud
from typing import Dict

def generate_wordcloud(cloud_input: Dict):
    wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(cloud_input)
    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud)
    plt.savefig("products_worldcloud.png")

def generate_sentiment_plot():
    pass

