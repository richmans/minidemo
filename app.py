from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

greetings = {'world': 'hello world'}

class Greeting(Resource):
    def get(self, greeting_id):
        return greetings[greeting_id]

    def put(self, greeting_id):
        greetings[greeting_id] = request.form['greeting']
        return {greeting_id: greetings[greeting_id]}

api.add_resource(Greeting, '/<string:greeting_id>')

if __name__ == '__main__':
    app.run(host="0.0.0.0")