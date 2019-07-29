from random import randint, choice

from flask_restplus import Resource
from mimesis import Address, Person
from flask import jsonify
from app.models.db_model import Puzzle
from app import db
from math import sin, cos, exp


class PuzzleResource(Resource):

    def get(self):
        puzzles = Puzzle.query.all()
        return jsonify({
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {
                        "stroke": "#555555",
                        "stroke-width": 2,
                        "stroke-opacity": 1,
                        "name": p.username,
                        "income": {
                            "2016": randint(100, 1000),
                        },
                    },
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [[[float(p.lon1), float(p.lat1)],
                                         [float(p.lon2), float(p.lat2)],
                                         [float(p.lon3), float(p.lat3)],
                                         [float(p.lon4), float(p.lat4)],
                                         [float(p.lon5), float(p.lat5)],
                                         [float(p.lon6), float(p.lat6)],
                                         [float(p.lon1), float(p.lat1)]
                                         ]
                                        ]
                    }
                 }
                for p in puzzles
            ]
        })


class UpdateResource(Resource):

    def get(self):
        entries = 100
        update_db_with_new_entries(entries, Puzzle)
        return {'msg': f'Updated database with {entries} entries'}


class DemoResource(Resource):
    def get(self):
        x0, y0, x1, y1 = [0, 0, 360, 360]

        MAX_ITERATIONS = 32
        person = Person('en-ca')

        features = []
        response = {
            "type": "FeatureCollection",
            "features": []
        }
        for i in range(MAX_ITERATIONS):
            feature = {
                "type": "Feature",
                "properties": {
                    "name": person.full_name(),
                    "income": {
                        "2018": randint(1000, 1000000)
                    }
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": []
                }
            }
            if i > 11 and i % 2 == 0:
                y1 += 5
            if i % 2 == 1:
                x1 = x1 / 2
            elif i % 2 == 0:
                y1 = y1 / 2
            print(f'{i}: {[[x0 - 180, y0 - 90], [x1 - 180, y0 - 90], [x1 - 180, y1 - 90], [x0 - 180, y1 - 90]]}')
            feature["geometry"]["coordinates"] = [
                [[x0 - 180, y0 - 90],
                 [x1 - 180, y0 - 90],
                 [x1 - 180, y1 - 90],
                 [x0 - 180, y1 - 90],
                 [x0 - 180, y0 - 90]]
            ]
            features.append(feature)

        response["features"] = features
        return jsonify(response)


class AnotherDemoResource(Resource):

    def get(self):
        x0, y0, x1, y1 = [0, 0, 360, 360]

        MAX_ITERATIONS = 32

        features = []
        response = {
            "type": "FeatureCollection",
            "features": []
        }
        for i in range(MAX_ITERATIONS):
            color = ''.join(choice("0123456789ABCDEF") for _ in range(6))
            feature = {
                "type": "Feature",
                "properties": {
                    "stroke": "#555555",
                    "stroke-width": 2,
                    "stroke-opacity": 1,
                    "fill": f'#{color}',
                    "fill-opacity": 0.25
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": []
                }
            }
            if i > 11 and i % 2 == 0:
                y1 += 5

            if i % 2 == 1:
                x1 = x1 / 2
            elif i % 2 == 0:
                y1 = y1 / 2

            print(f'{i}: {[[x0 - 180, cos(y0 - 90)], [x1 - 180, y0 - 90], [x1 - 180, y1 - 90], [x0 - 180, y1 - 90]]}')
            feature["geometry"]["coordinates"] = [
                [[(x0 - 180) * cos(2 * 3.14159 * (x0) / 180), (y0 - 90)],
                 [(x1 - 180) * cos(2 * 3.14159 * (x1) / 180), (y0 - 90)],
                 [(x1 - 180) * cos(2 * 3.14159 * (x1) / 180), (y1 - 90)],
                 [(x0 - 180) * cos(2 * 3.14159 * (x0) / 180), (y1 - 90)],
                 [(x0 - 180) * cos(2 * 3.14159 * (x0) / 180), (y0 - 90)]]
            ]
            features.append(feature)

        response["features"] = features
        return jsonify(response)


def update_db_with_new_entries(count, database):
    # add 6 * count of lon and lat to the database
    input_list = []
    a = Address()
    basic_lon, basic_lat = a.coordinates().values()
    for i in range(count):

        person = Person('uk')
        lon1 = basic_lon + 40 * cos(i)
        lat1 = basic_lat + 40 * sin(i)
        input_list.append(database(
            username=person.full_name(),
            division_order=1,
            lon1=lon1,
            lat1=lat1,
            lon2=lon1 + 1,
            lat2=lat1 + 2,
            lon3=lon1 + 3,
            lat3=lat1 + 2,
            lon4=lon1 + 4,
            lat4=lat1 + 0,
            lon5=lon1 + 3,
            lat5=lat1 - 2,
            lon6=lon1 + 1,
            lat6=lat1 - 2,
                   ))
    db.session.add_all(input_list)
    db.session.commit()
