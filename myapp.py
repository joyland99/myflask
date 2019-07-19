from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/whereami')
def whereami():
    return 'Ghana!'

if __name__ == '__main__':
    app.run(port=5001, debug=True)