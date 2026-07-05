from flask import Flask, jsonify
from flask_restful import Resource, Api
from get_repo_service import get_repo_service_method

app = Flask(__name__)
api = Api(app)


class make_a_call(Resource):
    method = get_repo_service_method()

    def get(self):
        return self.method.get_repos()

api.add_resource(make_a_call, '/')

if __name__ == "__main__":
    app.run(debug=True)