from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

var = Flask(__name__)
@var.route('/',methods=["GET","POST"])
def index():

    url = "https://www.businesstoday.in/technology"
    req = requests.get(url)
    aas= BeautifulSoup(req.content,"html.parser")

    outer_data = aas.find_all("div",class_="widget-listing",limit=5)
    top5news=""
    for data in outer_data:
        news = data.div.h2.a.string
        top5news+="\u2022 "+news+"\n"
    return render_template("index.html" , news=top5news)
