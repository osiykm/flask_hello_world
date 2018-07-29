from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'osiykm'}
    posts = [
        {
            'author': {'username': 'JoJo'},
            'body': 'CHI NO SADAME!!!! JO!!! JO!!!'
        },
        {
            'author': {'username': 'Dio'},
            'body': 'It\' me Dio!!!'
        },
        {
            'author': {'username': 'Speedwagon'},
            'body': 'Fear'
        },
    ]
    return render_template('index.html', title='Test', user=user, posts=posts)
