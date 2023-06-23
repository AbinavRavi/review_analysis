from utils.utils import read_config
import subprocess

config_path = "./config.yml"
config = read_config(config_path)

model = config["model"]["english_model"]
subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
subprocess.run(["python", "-m", "spacy", "download",model], check=True)

