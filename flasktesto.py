from flask import Flask, render_template
import requests
import json
from operator import itemgetter

app = Flask(__name__)

@app.route('/')
def home():
    return "Yeah you don land!"

@app.route('/memes')
def meme():
    
    def get_meme():
        return itemgetter("url", "postLink", "title")(requests.request("GET", "https://meme-api.com/gimme").json())

    url, postLink, title = get_meme()
    return render_template('index.html', page_title="Ultimate Memes", url = url, postLink = postLink, title = title)

app.run(host = '0.0.0.0', port = 3000)
