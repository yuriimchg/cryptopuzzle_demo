from flask_restplus import Resource


class SmokeTest(Resource):

    def get(self):
        return {'test': 'smoke'}