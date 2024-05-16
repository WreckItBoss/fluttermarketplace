from market import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length = 30), unique = True, nullable = False)
    email_address = db.Column(db.String(length = 50), unique = True, nullable = False)
    password_hash = db.Column(db.String(length = 60), nullable = False)
    budget = db.Column(db.Integer(), nullable = False, default = 1000)
    items = db.relationship('Item', backref = 'owned_user', lazy = True)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False)
    barcode = db.Column(db.String(12), unique=True, nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    owner = db.Column(db.Integer(), db.ForeigKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'
    