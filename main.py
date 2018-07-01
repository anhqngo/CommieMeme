from flask import Flask, render_template
from get_url import get_url

app = Flask('testapp')

@app.route('/')
def index():
    return render_template('index.html',
                            variable1=get_url()[0],
                            variable2=get_url()[1],
                            variable3=get_url()[2],
                            )

if __name__ == '__main__':
    app.run()