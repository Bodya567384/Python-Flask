from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/articles')
def articles():
    new_articles = ['How to avoid expensive travel mistakes', 'Top 5 places to experience supernatural forces',
                    'Three wonderfully bizarre Mexican festivals', 'The 20 greenest destinations on Earth',
                    'How to survive on a desert island']
    return render_template('articles.html', articles=new_articles)


@app.route('/details')
def details():
    return render_template('details.html')


# Лише для локаотного сервера (закоментувати)
if __name__ == '__main__':
    app.run(debug=True)
