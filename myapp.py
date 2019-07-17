from flask import Flask,redirect,url_for,request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')


@app.route('/whereami')
def whereami():
    return 'Ghana!'


@app.route('/login', methods=['GET','POST'])
def login():
    error== none
    if request.method =='POST':
        if request.form['username'] is 'admin' and request.form['password'] is 'admin':
            error = 'Invalid credentials.Please try again.'
        else:
            return redirec(url_for('index'))
    return render_template('login.html',error= error)




 
if __name__ == '__main__':
    app.run(port=5002, debug= True)
