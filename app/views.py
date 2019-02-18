from flask import render_template 
from app import app 
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting top news
    top_news = get_news('general')
    business_news = get_news('business')
    sports_news = get_news('sports')
    health_news = get_news('health')
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title, top = top_news, business = business_news, sports = sports_news ,health = health_news )