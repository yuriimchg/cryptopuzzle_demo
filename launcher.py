from app import app
from app.config import host, debug


if __name__ == '__main__':
    app.run(host=host, port=5000, debug=debug)
