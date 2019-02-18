from flask import render_template 
from app import app 

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the news page and its data
    '''

    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('news.html', title = title)

    from .request import get_news

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting top news
    top_news = get_news('top')
    print(top_news)
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title,top = top_news)
  
  # Getting sports news
    breaking_news = get_news('top')
    print(top_news)
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title,top = top_news)

# Getting business news
    breaking_news = get_news('top')
    print(top_news)
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title,top = top_news)

# Getting health news
    breaking_news = get_news('top')
    print(top_news)
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title,top = top_news)
