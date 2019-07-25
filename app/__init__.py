from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

api = Api(app=app)

from app.resources.puzzle import PuzzleResource, UpdateResource
from app.resources.smoke_test import SmokeTest

api.add_resource(SmokeTest, '/api/v1.0/smoke_test')
api.add_resource(PuzzleResource, '/api/v1.0/cryptopuzzle')
api.add_resource(UpdateResource, '/api/v1.0/update_database')
