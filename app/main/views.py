from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_source,article_source,get_category,get_headlines

@app.route('/')
def index():
    title= "Zacs trendy news app"
    return render_template('index.html', title=title)