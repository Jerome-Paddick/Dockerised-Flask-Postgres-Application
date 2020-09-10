import json

from flask_script import Manager, Command
from flask_migrate import Migrate, MigrateCommand

from app.models import db
from app.app_factory import create_app
from app.models.wedding_gifts import Products

# Manager is a utility for creating command line utilities for flask

class PopulateDB(Command):
    """ populates db from products.json """
    """ python dbmanager.py populate_db """
    def run(self):
        with open('products.json', 'r') as f:
            products = json.load(f)
            for prod in products:
                p = Products(
                    id=prod['id'],
                    name=prod['name'],
                    brand=prod['brand'],
                    price=prod['price'],
                    in_stock_quantity=prod['in_stock_quantity'],
                )
                db.session.add(p)
                db.session.commit()

# we register 'db' to flask migrate (wrapper for alembic)
# python dbmanager.py db init -> initialise migrations folder
# python dbmanager.py db migrate  -> create migrations from models
# python dbmanager.py db upgrade -> update database to next version
# python dbmanager.py db downgrade -> downgrade db to prev version

def create_db_manager():
    app = create_app(register_blueprints=False)
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.add_command('populate_db', PopulateDB)
    return manager


if __name__ == '__main__':
    create_db_manager().run()
