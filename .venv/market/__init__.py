from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

from market import routes, models
def create_app():
    with app.app_context():
        db.create_all()
        # Check if the database is empty, then populate it
        if db.session.query(models.Item).count() == 0:
            item1 = models.Item(name="iPhone 10", price=500, barcode='101010448943', description="desc")
            item2 = models.Item(name="Laptop", price=1000, barcode='105510448943', description="desc2")
            db.session.add(item1)
            db.session.add(item2)
            db.session.commit()
    return app