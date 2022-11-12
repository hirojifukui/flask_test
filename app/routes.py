from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    # return ("Hello World!")

    return """
    <html>
        <head>
            <title> Home </title>
        </head>
        <body>
            <div><a href ="/about"> About </a></div>
            <div><a href ="/test"> Test Page <a></div>
            <div><a href ="/test2"> Test2 Page <a></div>
        </body>
    </html>
    """

@app.route('/about')
def about():
    return "About"

@app.route('/test')
def test():
    user = {'username': 'H'}
    age = 20
    # return "This is a about page"
    return render_template('test.html', user=user, age = age)

@app.route('/test2')
def test2():
    user = {'username': 'Seb'}
    sample_data = [
    {
    'author': {'username': 'Seb'},
    'body': 'Hello!'
    },
    {
    'author': {'username': 'H'},
    'body': 'Welcome to Flask!'
    }
    ]
    return render_template('test2.html', user=user, sample_data=sample_data)
