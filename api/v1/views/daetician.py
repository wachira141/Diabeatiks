#!/usr/bin/python3
from flask import make_response, request, jsonify, json, abort
from api.v1.views import app_views
from models.daetician import Daetician
from models import storage



@app_views.route('/daeticians', methods=['GET'], strict_slashes=False)
def get_daetician():
    """get all daetician's from our storage"""
    daeticians = storage.all(Daetician)
    items = []

    for obj in daeticians:
        items.append(obj.to_dict())
    return json.dumps(items)

@app_views.route('/daetician/<id>', methods=['GET'], strict_slashes=False)
def get_daetician(id):
    """get a single object of a daetician"""
    daetician = storage.get(Daetician, id)
    if daetician is None:
        return make_response(jsonify("No Patient with an id of {}".format(id)))
    return json.dumps(daetician.to_dict(), 200)
    

@app_views.route('/daetician', methods=['POST'], strict_slashes=False)
def create_daetician():
    """create a new daetician """
    if not request.get_json():
        abort(400, description='please provide a valid json format')
    if 'f_name' or 'l_name' not in request.get_json():
        abort(400, description='please provide all names')
    
    if 'email' not in request.get_json():
        abort(400, description='email is not provided')
    # check the email format
    data = request.get_json()
    new_daetician = Daetician(**data)
    new_daetician.save()

    return make_response(json.dumps(new_daetician.to_dict()), 201)

  

@app_views.route('/daetician/<id>', methods=['PUT'], strict_slashes=False)
def update_daetician(id):
    """update daetician's details"""
    if not request.get_json():
        abort(400, description='please provide a valid json')
    daetician = storage.get(Daetician, id)
    if daetician is None:
        abort(400, description='No patient with an id of {}'.format(id))
    
    data = request.get_json()
    for key, val in daetician:
        if key is not 'id' or key is not 'created_at' or key is not 'updated_at':
            setattr(data, key, val)
    return make_response(json.dumps(data.to_dict()), 200)
    



@app_views.route('/patient/<id>', methods=['DELETE'], strict_slashes=False)
def  delete_daetician(id):
    """delete a daetician based on id"""
    if not request.get_json():
        abort(400, description='please provide a valid json')

    daetician = storage.get(Daetician, id)

    if daetician is None:
        abort(400, description='No patient with an id of {}'.format(id))
    
    storage.delete(daetician, id)

