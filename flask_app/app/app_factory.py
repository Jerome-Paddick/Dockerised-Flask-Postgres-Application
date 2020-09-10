from flask import Flask
from flask_restful import Api
from .models.core import db
from flask_restful_swagger import swagger

def create_app(register_blueprints=True):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('app.default_config')
    # app.config.from_pyfile('application.cfg.py')

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        "{db_prefix}://{user}:{passwd}@{server}/{db}".format(
        db_prefix=app.config['SQLALCHEMY_DB_PREFIX'],
        user=app.config['POSTGRES_USER'],
        passwd=app.config['POSTGRES_PASSWORD'],
        server=app.config['DB_SERVER'],
        db=app.config['POSTGRES_DB'])
    db.init_app(app)

    # so we can call current_app.db from any resource
    app.db = db

    # api = Api(app)

    # Swagger flask restful API:
    # https://github.com/rantav/flask-restful-swagger
    api = swagger.docs(
        Api(app),
        apiVersion='1.0',
        api_spec_url='/api/api_documentation',
        swaggerVersion='3.0',
        description='Cloud API'
    )

    from .resources.gifts import GiftsResource
    from .resources.gifts import PutRemoveGiftsResource
    api.add_resource(GiftsResource, '/api/gifts')
    api.add_resource(PutRemoveGiftsResource, '/api/gifts/<gift_id>')


    from .resources.gifts import GiftsReportResource
    api.add_resource(GiftsReportResource, '/api/gift-report')

    return app
