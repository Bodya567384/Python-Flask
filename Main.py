from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def index():
    n = random.randint(0, 1000)
    k = random.randint(1000, 5000)
    # return f"<h1>My page [{n}]</h1>"
    return render_template('index.html', n=n, k=k)


@app.route('/login')
def about():
    return render_template('login.html')


# Лише для локального сервера (закометувати)
if __name__ == '__main__':
    app.run(debug=True)
