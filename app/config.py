debug = True
database = "cryptopuzzle_sandbox"
user = "yurii"
password = "yurii"
host = "127.0.0.1"
port = "5432"
SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}/{database}'
SQLALCHEMY_TRACK_MODIFICATIONS=False
