debug = True
database = "demo_database"
user = "demo_user"
password = "demo_password"
host = "localhost"
port = "5432"
SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}/{database}'
SQLALCHEMY_TRACK_MODIFICATIONS=False
