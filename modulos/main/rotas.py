from flask import render_template
from .main import main

@main.route("/")
def home():
    return render_template('main_home.html')
