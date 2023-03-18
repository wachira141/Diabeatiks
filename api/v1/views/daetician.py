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
    return make_response(json.dumps(items), 200)

@app_views.route('/daetician/<id>', methods=['GET'], strict_slashes=False)
def get_daetician(id):
    """get a single object of a daetician"""
    daetician = storage.get(Daetician, id)
    if daetician is None:
        return make_response(jsonify("No Patient with an id of {}".format(id)), 404)
    return json.dumps(daetician.to_dict(), 200)
    

@app_views.route('/daetician', methods=['POST'], strict_slashes=False)
def create_daetician():
    """create a new daetician """
    if not request.get_json():
        abort(400, description='please provide a valid json format')
   
    names = ['f_name', 'l_name']
    for name in names:
        if name not in request.get_json():
            abort(400, description='please provide {}'.format(name))

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
        abort(404, description='No patient with an id of {}'.format(id))
    
    data = request.get_json()

    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, val in data.items():
        if key not in ignore_keys:
            setattr(daetician, key, val)
    storage.save
    return make_response(json.dumps(daetician.to_dict()), 200)
    
    



@app_views.route('/daetician/<id>', methods=['DELETE'], strict_slashes=False)
def  delete_daetician(id):
    """delete a daetician based on id"""

    daetician = storage.get(Daetician, id)

    if daetician is None:
        abort(400, description='No Daetician with an id of {}'.format(id))
    
    item_deleted = storage.delete('Daetician', id)

    if item_deleted is None:
        abort(400, description='Daetician with an id of {} not deleted'.format(id))

    return make_response(json.dumps("daetician deleted successfully"), 200)
    



