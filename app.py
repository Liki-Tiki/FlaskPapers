from flask import Flask, render_template
from data import Articless ##recupere le data dans la var

app = Flask(__name__)
app.debug=True

Articles = Articless()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles) #met le stock data dans la var html

@app.route('/article/<string:id>/') #route pour un article en particulier
def article(id):
    return render_template('article.html', id=id)

if __name__ == '__main__':
    app.run()
