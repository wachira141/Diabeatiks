#!/usr/bin/python3
from flask import make_response, request, jsonify, json, abort
from api.v1.views import app_views
from models.location import Location
from models.village import Village
from models import storage



@app_views.route('/location/<location_id>/village', methods=['POST'], strict_slashes=False)
def create_village(location_id):
    """create a village object"""
    if not request.get_json():
        abort(400, descriptions='please provide a valid json')
    
    data = request.get_json()


 # check if location exists
    location = storage.get(Location, location_id)
    if location is None:
        return abort(404, description='no location with an id of {}'.format(location_id))

    
    new_village = Village(**data)
    new_village.location = location.to_dict()['id']
    new_village.save()

    return make_response(json.dumps(new_village.to_dict()), 201)



@app_views.route('/village/<id>', methods=['GET'], strict_slashes=False)
def get_village(id):
    """get a village by id"""
    village = storage.get(Village, id)
    if village is None:
        abort(400, description='No village found')
    return make_response(json.dumps(village.to_dict()), 200)



@app_views.route('/location/<location_id>/village', methods=['GET'], strict_slashes=False)
def get_all_locations(location_id):
    """get all subcounties in a county referenced by an county_id"""
    location = storage.get(Location, location_id)

    if location is None:
        abort(404, description='location not found')
    
    villages = storage.all(Village).values()
    vil_list = []
    for vl in villages:
        if vl.to_dict()['location'] == location_id:
            vil_list.append(vl.to_dict())

    return make_response(json.dumps(vil_list), 200)




@app_views.route('/village<id>', methods=['PUT'], strict_slashes=False)
def update_village(id):
    """update village's details"""
    if not request.get_json():
        abort(400, description='please provide a valid json')
    village = storage.get(Village, id)
    if village is None:
        abort(400, description='No village with an id of {}'.format(id))
    
    data = request.get_json()
    ignore_keys = ['location','created_at', 'updated_at', 'id']

    for key, val in data.items():
        if val not in ignore_keys:
            setattr(village, key, val)
    storage.save()
    return make_response(json.dumps(village.to_dict()), 200)


@app_views.route('/village/<id>', methods=['DELETE'], strict_slashes=False)
def delete_village(id):
    """delete a village based on id"""

    village = storage.get(Village, id)

    if village is None:
        abort(400, description='No village with an id of {}'.format(id))
    
    item_deleted = storage.delete('Village', id)

    if item_deleted is None:
        abort(400, description='village with an id of {} not deleted'.format(id))

    return make_response(json.dumps("village deleted successfully"), 200)





