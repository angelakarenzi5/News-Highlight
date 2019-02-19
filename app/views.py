from flask import render_template,request,redirect,url_for
from app import app 
from .request import get_sources, get_source, search_source

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
    return render_template('index.html',title = title, general = general_news, business = business_news, sports = sports_news ,health = health_news )

    title = 'Home - Welcome to The best News Review Website Online'

    search_source = request.args.get('source_query')

    if search_source:
        return redirect(url_for('search',source_name=search_source))
    else:
        return render_template('index.html',title = title, general = general_news, business = business_news, sports = sports_news ,health = health_news )

@app.route('/source/<id>')
def source(id):

    '''
    View source page function that returns the source details page and its data
    '''
    source = get_sources(id)
    name = f'{source.name}'

    return render_template('source.html',name = name,source = source)

@app.route('/search/<source_name>')
def search(source_name):
    '''
    View function to display the search results
    '''
    source_name_list = source_name.split(" ")
    source_name_format = "+".join(source_name_list)
    searched_sources = search_source(source_name_format)
    title = f'search results for {source_name}'
    return render_template('search.html',sources = searched_sources)