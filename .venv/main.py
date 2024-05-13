from flask import Flask
app = Flask(__name__)

@app.route('/')
def hell_world():
    return "<h1> Hello World! </h1>"

@app.route('/about')
def about_page():
    return "<h1> About page </h1>"

if __name__=='__main__':
    app.run(debug=True)