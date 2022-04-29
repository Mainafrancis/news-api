from ..request import get_news
from . import main
from flask import render_template, request
from ..models import News_Article

# Viewscategory=business category=science category=sports entertainment

@main.route('/')
def index():
    business_news = get_news('business')
    science_news = get_news('science')
    entertainment_news = get_news('entertainment')
    title = 'Welcome to the news platform'
    return render_template('index.html', business=business_news, science=science_news, entertainment=entertainment_news)