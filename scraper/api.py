from flask import Flask
from flask_restful import Api, Resource
from .scraper import scrap


app = Flask(__name__)
api = Api(app)


class Prices(Resource):

    @staticmethod
    def get(name):

        return scrap(name)


api.add_resource(Prices, "/price/<name>")

if __name__ == '__main__':
    # app.run(debug=True, host="127.0.0.1")   # Development

    # Product
    from waitress import serve

    serve(app, host="127.0.0.1", port=5000)

