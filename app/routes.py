from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'osiykm'}
    return '''
    <html>
        <head>
        <title>Test page</title>
        <body>
            <h1>Hello ''' + user['username'] + '''</h1>
        </body>
        </head>
    </html>
    '''
