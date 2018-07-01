from flask import Flask, render_template
from get_url import get_url

app = Flask('testapp')

@app.route('/')
def index():
    return render_template('index.html', variable=get_url())

if __name__ == '__main__':
    app.run()