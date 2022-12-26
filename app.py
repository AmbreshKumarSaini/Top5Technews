from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

var = Flask(__name__)
@var.route('/',methods=["GET","POST"])
def index():

    url = "https://www.news18.com/tech"
    req = requests.get(url)
    soup= BeautifulSoup(req.content,"html.parser")

    outer_data = soup.find_all("div",class_="jsx-3621759782 blog_list_row",limit=5)
    top5news=""
    for data in outer_data:
        news = data.a.figure.figcaption.div.h4.string
        top5news+="\u2022 "+news+"\n"
    return render_template("index.html" , news=top5news)
