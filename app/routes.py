from app import app
from flask import request, render_template

from app.logic import get_weather, get_news, get_quotes


@app.route('/', methods=['GET', 'POST'])
#function for save weather
def index():
    weather = None
    news = None
    quotes = None

    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        news = get_news()
        quotes = get_quotes()
    return render_template('index.html', weather=weather, news=news, quotes=quotes)




