import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    #login data
    username = db.Column(db.Text)
    password = db.Column(db.Text)
    #account info
    discord = db.Column(db.Text)
    description = db.Column(db.Text)
    communityUsers = db.relationship("Test_User", backref="user")

    def __init__(self, username, password):
        self.username = username
        self.password = password
        #blank info
        self.discord = "none"
        self.description = "HI, i'm new to this webite!"

    def __repr__(self):
        return f"username: {self.username}, password: {self.password}\n"
'''
class InventorySlot(db.Model):
    __tablename__ = "inventory"

    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer, db.ForeignKey("users.id"))
    itemId = db.Column(db.Integer, db.ForeignKey("items.id"))

    def __init__(self, owner, itemId):
        self.owner = owner
        self.itemId = itemId

    def __repr__(self):
        return f"Owner: {self.owner}, Item: {self.itemId}\n"

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    value = db.Column(db.Integer)

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"name: {self.name}, value: {self.value}\n"
'''

# Test Community
# Eventrually i mgoing to make a community model for all the models that seort them by community
class Test_User(db.Model):
    __tablename__ = "test_users"
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"))
    rank = db.Column(db.Integer)
    trades = db.relationship("Test_Trades", backref="ownerId")
    #reports = db.relationship("Test_Report", backref="ownerId")

    def __init__(self, user, rank):
        self.user = user
        self.rank = rank
'''
class Test_Report(db.Model):
    __tablename__ = "test_reports"
    id = db.Column(db.Integer, primary_key=True)
    reporter = db.Column(db.Integer, db.ForeignKey("test_users.id"))
    scammer = db.Column(db.Integer, db.ForeignKey("test_users.id"))
    description = db.Column(db.Text)
    videoLink = db.Column(db.Text)

    def __init__(self, reporter, scammer, description, videoLink):
        self.reporter = reporter
        self.scammer = scammer
        self.description = description
        self.videoLink = videoLink
'''
class Test_Trades(db.Model):
    __tablename__ = "test_trades"

    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer, db.ForeignKey("test_users.id"))
    items = db.relationship("Test_ItemForTrade", backref="trade")

    def __init__(self, owner):
        self.owner = owner
        
class Test_ItemForTrade(db.Model):
    __tablename__ = "test_itemsForTrade"

    id = db.Column(db.Integer, primary_key=True)
    tradeId = db.Column(db.Integer, db.ForeignKey("test_trades.id"))
    owner = db.Column(db.Integer, db.ForeignKey("test_users.id"))
    item = db.Column(db.Integer, db.ForeignKey("test_items.id"))

    def __init__(self, owner, item, tradeId):
        self.owner = owner
        self.item = item
        self.tradeId = tradeId

class Test_Items(db.Model):
    __tablename__ = "test_items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    price = db.Column(db.Integer)
    image = db.Column(db.Text)

    def __init__(self, name, price, image):
        self.name = name
        self.price = price
        self.image = image

    def __repr__(self):
        return f"{self.name}, {self.price}, {self.image}\n"


'''
class Test_Message(db.Model):
    __tablename__ = "test_Chat"

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey("test_users.id"))
    message = db.Column(db.Text)
    time = db.Column(db.Text)

    def __init__(self, user, message, time):
        self.user = user
        self.message = message
        self.time = time
'''