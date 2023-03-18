#!/usr/bin/python3
from flask import make_response, request, jsonify, json, abort
from api.v1.views import app_views
from models.county import County
from models import storage



@app_views.route('/county', methods=['POST'], strict_slashes=False)
def create_county():
    """create a county object"""
    if not request.get_json():
        abort(400, descriptions='please provide a valid json')
    
    data = request.get_json()

    counties = storage.all(County).values()
    for obj in counties:
        if obj.to_dict()['name'] == data.get('name'):
            return abort(400, description='{} county already added'.format(data['name']))
    
    new_county = County(**data)
    new_county.save() 

    return make_response(json.dumps(new_county.to_dict()), 201)


@app_views.route('/county/<id>', methods=['GET'], strict_slashes=False)
def get_county(id):
    """get a county by id"""
    county = storage.get(County, id)
    if county is None:
        abort(400, description='No county  with an id of {} found'.format(id))
    return make_response(json.dumps(county.to_dict()), 200)



@app_views.route('/county/<id>', methods=['PUT'], strict_slashes=False)
def update_county(id):
    """update county's details"""
    if not request.get_json():
        abort(400, description='please provide a valid json')
    county = storage.get(County, id)
    if county is None:
        abort(400, description='No county with an id of {}'.format(id))
    
    data = request.get_json()
    

    ignore_keys = ['id', 'created_at', 'updated_at']

    for key, val in data.items():
        if key not in ignore_keys:
            setattr(county, key, val)
    storage.save
    return make_response(json.dumps(county.to_dict()), 200)

@app_views.route('/county/<id>', methods=['DELETE'], strict_slashes=False)
def delete_county(id):
    """delete a county based on id"""

    county = storage.get(County, id)

    if county is None:
        abort(400, description='No County with an id of {}'.format(id))
    
    item_deleted = storage.delete('County', id)

    if item_deleted is None:
        abort(400, description='County with an id of {} not deleted'.format(id))

    return make_response(json.dumps("County deleted successfully"), 200)





