from flask import render_template
from . import main
from ..requests import get_sources, get_specific_source

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    sources_list = get_sources()
    title = 'News Sources'
    return render_template('index.html', sources = sources_list, title= title)


@main.route('/source/<name>')
def source(name):
    articles_list = get_specific_source(name)
    if len(articles_list) > 0:
        source = articles_list[0].source['name']
    else:
        source = None
    title = f"{name} articles"
    return render_template('articles.html', articles = articles_list, title=title, source = source)
