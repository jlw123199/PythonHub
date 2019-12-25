from flask import Flask

app = Flask(__name__)

# @app.route('/users/<string:username>')
@app.route('/', methods=['GET'])
def hello_world(username=None):
      return("Hello {}!".format(username))


app.run(host='127.0.0.1',port=2480)