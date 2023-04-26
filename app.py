from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

websites = ['https://techcrunch.com/search', 'https://gizmodo.com/',
            'https://www.theverge.com/search?q=', 'https://venturebeat.com/?s=', 'https://www.wired.com/search/?q=', 'https://mashable.com/search?query=']


@app.route("/search/<tag>")
def make_request(tag):
    if " " in tag:
        tag = tag.replace(" ", "+")
    rq = requests.get(websites[-1]+tag)
    soup = BeautifulSoup(rq.content, "html.parser")
    articles_titles = soup.find_all(
        "a", class_="block text-primary-400 font-semibold leading-6 text-lg header-500 md:text-xl")
    articles_desc = soup.find_all(
        "div", class_="hidden text-base md:block md:mt-1 md:leading-tight text-primary-400 font-regular")
    titles = [a.text.strip() for a in articles_titles]
    desc = [a.text.strip() for a in articles_desc]
    return dict(zip(titles, desc))
