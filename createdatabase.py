from app import app
from models import db, User, Item, InventorySlot

test = User('test', 'test')
db.session.add(test)
db.session.commit()

'''
alex = User.query.filter_by(username='alexthegreat194').first()
roka = Item.query.filter_by(name='Roka').first()
print(alex)
print(roka)

slot = InventorySlot(alex.id, roka.id)
print(slot)
db.session.add(slot)
db.session.commit()

print(alex)
print(roka)

print("Done")
'''