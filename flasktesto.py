from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Yeah you don land!"

app.run(host = '0.0.0.0', port = 3000)