from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_source,article_source,get_category,get_headlines

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # title= "Zacs trendy news app"
    source= get_source()
    headlines = get_headlines()
    return render_template('index.html', source=source, headlines=headlines)