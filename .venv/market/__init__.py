from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

from market import routes, models
def create_app():
    with app.app_context():
        db.drop_all()
        db.create_all()
        # Check if the database is empty, then populate it
        if db.session.query(models.Item).count() == 0:
            item1 = models.Item(name="iPhone 10", price=500, barcode='101010448943', description="desc")
            item2 = models.Item(name="Laptop", price=1000, barcode='105510448943', description="desc2")
            db.session.add(item1)
            db.session.add(item2)
            db.session.commit()
        if db.session.query(models.User).count() == 0:
            user1 = models.User(username='jsc', password_hash='123456', email_address='jsc@jsc.com')
            db.session.add(user1)
            db.session.commit()
        print(models.User.query.all()) 
    return app