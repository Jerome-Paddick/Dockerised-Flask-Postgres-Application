from .core import db
# from sqlalchemy.orm import relationship

class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    in_stock_quantity = db.Column(db.Integer, nullable=False)

class Gifts(db.Model):
    __tablename__ = 'gifts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.ForeignKey('products.id'), nullable=False)
    purchased = db.Column(db.Boolean, nullable=False, default=False)
    product = db.relationship('Products')