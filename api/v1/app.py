from flask import Flask, render_template, jsonify, make_response
import json
from api.v1.views import app_views
from models import storage

app = Flask(__name__)

app.register_blueprint(app_views)


app.teardown_appcontext
def tear_down(error):
    """close db on app teardown"""
    storage.close()

app.errorhandler
def _404_error(error):
    """not found error response"""
    return make_response(jsonify({"error":"Not found"}), 404)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)