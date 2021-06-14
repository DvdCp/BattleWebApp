from Esercizio5.resources.Arena import Arena
from Esercizio5 import app
from flask_restful import Api
from flask import make_response, render_template

import Esercizio5.utils.DatabaseHelper as DBHelper

exposedApi = Api(app)

# Adding resources to API
exposedApi.add_resource(Arena, "/Arena")

if __name__ == "__main__":
    DBHelper.createDb()
    app.run(debug=True)
