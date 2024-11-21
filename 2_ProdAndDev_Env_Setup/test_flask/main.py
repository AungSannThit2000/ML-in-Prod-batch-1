from flask import Flask
from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)
@app.get("/")
def home():
    str_out = "This is {} server : {}".format(os.getenv("ENV"),os.getenv("VER"))
    return str_out

app.run("")