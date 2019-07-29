from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)

app.config.from_pyfile('config.py')
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

cors = CORS(app, resources={r'/api/*': {'origins': '*'}})
api = Api(app=app)

from app.resources.puzzle import PuzzleResource, UpdateResource, DemoResource, AnotherDemoResource
from app.resources.smoke_test import SmokeTest

api.add_resource(SmokeTest, '/api/v1.0/smoke_test')
api.add_resource(PuzzleResource, '/api/v1.0/cryptopuzzle')
api.add_resource(UpdateResource, '/api/v1.0/update_database')
api.add_resource(DemoResource, '/api/v1.0/demo_resource')
api.add_resource(AnotherDemoResource, '/api/v1.0/demo_resource_two')
