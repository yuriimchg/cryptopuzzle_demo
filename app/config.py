debug = True
database = "cryptopuzzle_sandbox"
user = "yurii"
password = "yurii"
host = "0.0.0.0"
port = "5432"
SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}/{database}'
SQLALCHEMY_TRACK_MODIFICATIONS=False
