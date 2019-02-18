from flask import render_template 
from app import app 

# Views
@app.route('/')
def news():

    '''
    View root page function that returns the news page and its data
    '''

    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('news.html', title = title)
