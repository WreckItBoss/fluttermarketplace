from market import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length = 30), unique = True, nullable = False)
    

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False)
    barcode = db.Column(db.String(12), unique=True, nullable=False)
    description = db.Column(db.String(1024), nullable=True)

    def __repr__(self):
        return f'Item {self.name}'
    