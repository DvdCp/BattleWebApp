from flask_restful import Api
from flaskr.resources.Arena import Arena
from flaskr import app
import flaskr.utils.DatabaseHelper as DBHelper


exposedApi = Api(app)
# Adding resources to API
exposedApi.add_resource(Arena, "/")

if __name__ == "__main__":
    DBHelper.createDb()
    app.run(debug=True)
