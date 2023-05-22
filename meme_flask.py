from flask import Flask
import requests
import json

app = Flask(__name__)

def get_meme():
    #Uncomment these two lines and comment out the other url line if you want to use a specific meme subreddt
    sr = "/Demotivational"
    url = "<https://meme-api.herokuapp.com/gimme>" + sr
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

@app.route("/")
def index():
    meme_pic,subreddit = get_meme()
    return render_template("meme_index.html",
    meme_pic=meme_pic,
    subreddit=subreddit)