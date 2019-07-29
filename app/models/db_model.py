from app import db


class Puzzle(db.Model):
    __tablename__ = 'fractals'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False, unique=False)
    division_order = db.Column(db.Integer, nullable=False)

    lon1 = db.Column(db.DECIMAL, nullable=False)
    lat1 = db.Column(db.DECIMAL, nullable=False)

    lon2 = db.Column(db.DECIMAL, nullable=False)
    lat2 = db.Column(db.DECIMAL, nullable=False)

    lon3 = db.Column(db.DECIMAL, nullable=False)
    lat3 = db.Column(db.DECIMAL, nullable=False)

    lon4 = db.Column(db.DECIMAL, nullable=False)
    lat4 = db.Column(db.DECIMAL, nullable=False)

    lon5 = db.Column(db.DECIMAL, nullable=False)
    lat5 = db.Column(db.DECIMAL, nullable=False)

    lon6 = db.Column(db.DECIMAL, nullable=False)
    lat6 = db.Column(db.DECIMAL, nullable=False)


class DemoFractal(db.Model):
    __tablename__ = 'demo_fractals'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False, unique=False)
    division_order = db.Column(db.Integer, nullable=False)

    lon1 = db.Column(db.DECIMAL, nullable=False)
    lat1 = db.Column(db.DECIMAL, nullable=False)

    lon2 = db.Column(db.DECIMAL, nullable=False)
    lat2 = db.Column(db.DECIMAL, nullable=False)

    lon3 = db.Column(db.DECIMAL, nullable=False)
    lat3 = db.Column(db.DECIMAL, nullable=False)

    lon4 = db.Column(db.DECIMAL, nullable=False)
    lat4 = db.Column(db.DECIMAL, nullable=False)
