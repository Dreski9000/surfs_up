from flask import Flask

# create new flask app instance

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

