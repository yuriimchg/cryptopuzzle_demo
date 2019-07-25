debug = True
database = "cryptopuzzle_sandbox"
user = "yurii"
password = "yurii"
host = "194.44.111.78"
port = "5432"
SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}/{database}'
SQLALCHEMY_TRACK_MODIFICATIONS=False
