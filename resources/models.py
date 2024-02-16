from resources import db


class Customers(db.Model):
    __tablename__ = 'customer_accounts'
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=True)
    username = db.Column(db.String(250), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    image_file = db.Column(db.String(120), nullable=True, default='default.jpg')
    password = db.Column(db.String(250), unique=False, nullable=True)
    document = db.Column(db.String(250), unique=False, nullable=True)
