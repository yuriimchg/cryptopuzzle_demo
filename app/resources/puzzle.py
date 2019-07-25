from random import randint

from flask_restplus import Resource
from mimesis import Address, Person
from flask import jsonify
from app.models.db_model import Puzzle
from app import db


class PuzzleResource(Resource):

    def get(self):
        puzzles = Puzzle.query.all()
        return jsonify({
            "type": "FeatureCollection",
            "features": [
                {
                    "properties":
                    {
                        "name": p.username,
                        "income": {
                            "2016": randint(10, 100),
                        },
                        "geometry": {
                            "type": "Hexagon",
                            "coordinates": [[[float(p.lon1), float(p.lat1)],
                                             [float(p.lon2), float(p.lat2)],
                                             [float(p.lon3), float(p.lat3)],
                                             [float(p.lon4), float(p.lat4)],
                                             [float(p.lon5), float(p.lat5)],
                                             [float(p.lon6), float(p.lat6)],
                                             ]]

                        }

                    }
                 }
                for p in puzzles
            ]
        })


class UpdateResource(Resource):

    def get(self):
        entries = 1000
        update_db_with_new_entries(entries)
        return {'msg': f'Updated database with {entries} entries'}


def update_db_with_new_entries(count):
    # add 6 * count of lon and lat to the database
    input_list = []
    for _ in range(count):
        a = Address()
        person = Person('en')
        lon1, lat1 = a.coordinates().values()

        input_list.append(Puzzle(
            username=person.full_name(),
            division_order=1,
            lon1=lon1,
            lat1=lat1,
            lon2=lon1+1,
            lat2=lat1+2,
            lon3=lon1+3,
            lat3=lat1+2,
            lon4=lon1+1,
            lat4=lat1-2,
            lon5=lon1+3,
            lat5=lat1-2,
            lon6=lon1+4,
            lat6=lat1+0,
                   ))
    db.session.add_all(input_list)
    db.session.commit()
