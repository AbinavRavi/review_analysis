import matplotlib.pyplot as plt
from wordcloud import WordCloud
from typing import Dict

def generate_wordcloud(cloud_input: Dict):
    wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(cloud_input)
    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud)
    plt.savefig("products_worldcloud.png")

def generate_bar_plot(input_dict: Dict, title: str):
    x = list(input_dict.keys())
    y = list(input_dict.values())
    plt.bar(x, y)
    plt.xticks(rotation=90)
    plt.title(title)
    plt.show()
    plt.savefig(f"{title}.png")

