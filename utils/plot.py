import matplotlib.pyplot as plt
from wordcloud import WordCloud
from typing import Dict

def generate_wordcloud(cloud_input: Dict, name):
    wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(cloud_input)
    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud)
    plt.savefig(f"plots/{name}.png")

def generate_bar_plot(input_dict: Dict, title: str):
    x = list(input_dict.keys())
    y = list(input_dict.values())
    plt.figure(figsize=(20,10))
    plt.bar(x, y)
    plt.xticks(rotation=90)
    plt.title(title)
    plt.show()
    plt.savefig(f"plots/{title}.png")

