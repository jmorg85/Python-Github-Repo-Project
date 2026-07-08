from flask import Flask, jsonify
from flask_restful import Resource, Api
from get_repo_service import get_repo_service_method
import asyncio

app = Flask(__name__)
api = Api(app)


class make_a_call(Resource):
    method = get_repo_service_method()

    def get(self):
        names = []
        results = asyncio.run(self.method.get_repos()) #Turns out flask produces a synchronous wrapper on it's endpoints. So to fix this, you make the method async and do an async call within it it.

        for result in results:
            names.append(result['name'])
            
        return jsonify(names)

api.add_resource(make_a_call, '/')

if __name__ == "__main__":
    app.run(debug=True)