from app import app
from flask import render_template

@app.route('/')
def home():
    foods = ['burger','hotdog']
    return render_template('index.html', foods=foods)