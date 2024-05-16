from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False)
    barcode = db.Column(db.String(12), unique=True, nullable=False)
    description = db.Column(db.String(1024), nullable=True)

    def __repr__(self):
        return f'Item {self.name}'
    





@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')
@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template('market.html', items = items)

if __name__=='__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
    