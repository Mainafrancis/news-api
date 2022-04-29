from ..request import get_news
from . import main
from flask import render_template, request
from ..models import News_Article

# Viewscategory=business category=science category=sports entertainment

@main.route('/')
def index():
    business_news = get_news('business')