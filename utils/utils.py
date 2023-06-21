import yaml

def read_config(file):
    with open(file,'r') as stream:
        config = yaml.full_load(stream)
    return config

def read_text_file(file):
    with open(file, "r", encoding="utf-8") as file:
        reviews_text = file.read()
    return reviews_text

