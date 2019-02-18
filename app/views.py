from flask import render_template 
from app import app 
from .request import get_sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting general news
    general_news = get_sources('general')
    business_news = get_sources('business')
    sports_news = get_sources('sports')
    health_news = get_sources('health')
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title, general = general_news, business = business_news, sports = sports_news ,health = health_news )