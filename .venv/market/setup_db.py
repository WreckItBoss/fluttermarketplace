from market import app, db
from market.models import Item

with app.app_context():
    db.drop_all()
    db.create_all()
    item1 = Item(name = "iPhone 10", price = 500, barcode = '101010448943', description = "desc")
    item2 = Item(name = "Laptop", price = 1000, barcode = '105510448943', description = "desc2")
    db.session.add(item1)
    db.session.add(item2)
    db.session.commit()
    db.session.commit()
    print(Item.query.all()) 
