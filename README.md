##### Prerequired setup: 
* Python 3.7
* git
* Postgresql 11

#### How to launch demo:


1. Clone the app from github:
```
git clone https://github.com/yurmchg/cryptopuzzle_demo.git
```
2. Create a virtual environment and launch it:
```
cd cryptopuzzle_demo
python3.7 -m venv venv
source venv/bin/activate
```
3. Setup a database:
```
createuser demo_user --createdb --createrole --pwprompt
createdb demo_database --owner=demo_user --username=demo_user 
```
4. Initialize the app:
```
export FLASK_APP=launcher.py
flask db init
flask db migrate -m 'initial migration'
flask db upgrade
```

5. Run the app:
```
flask run
```

The API is available on the localhost:
* http://127.0.0.1:5000/api/v1.0/cryptopuzzle
* http://127.0.0.1:5000/api/v1.0/demo_resource
