#!/usr/bin/python3
from flask import make_response, request, jsonify, json, abort
from api.v1.views import app_views
from models.location import Location
from models.subcounty import Subcounty
from models import storage



@app_views.route('/subcounty/<subcounty_id>/location', methods=['POST'], strict_slashes=False)
def create_location(subcounty_id):
    """create a location object"""
    if not request.get_json():
        abort(400, descriptions='please provide a valid json')
    
    data = request.get_json()


 # check if subcounty exists
    subcounty = storage.get(Subcounty, subcounty_id)
    if subcounty is None:
        return abort(404, description='no subcounty with an id of {}'.format(subcounty_id))

    
    new_location = Location(**data)
    new_location.subcounty = subcounty.to_dict()['id']
    new_location.save()

    return make_response(json.dumps(new_location.to_dict()), 201)


@app_views.route('/location/<id>', methods=['GET'], strict_slashes=False)
def get_location(id):
    """get a location by id"""
    location = storage.get(Location, id)
    
    if location is None:
        abort(400, description='No location found')
    return make_response(json.dumps(location.to_dict()), 200)




@app_views.route('/subcounty/<subcounty_id>/location', methods=['GET'], strict_slashes=False)
def get_all_locations(subcounty_id):
    """get all subcounties in a county referenced by an county_id"""
    subcounty = storage.get(Subcounty, subcounty_id)

    if subcounty is None:
        abort(404, description='subcounty not found')
    
    location = storage.all(Location).values()
    loc_list = []
    for loc in location:
        if loc.to_dict()['subcounty'] == subcounty_id:
            loc_list.append(loc.to_dict())

    return make_response(json.dumps(loc_list), 200)




@app_views.route('/location/<id>', methods=['PUT'], strict_slashes=False)
def update_location(id):
    """update locations's details"""
    if not request.get_json():
        abort(400, description='please provide a valid json')
    location = storage.get(Location, id)
    if location is None:
        abort(400, description='No location with an id of {}'.format(id))
    
    data = request.get_json()
    ignore_keys = ['subcounty','created_at', 'updated_at', 'id']

    for key, val in data.items():
        if val not in ignore_keys:
            setattr(location, key, val)
    storage.save()
    return make_response(json.dumps(location.to_dict()), 200)


@app_views.route('/location/<id>', methods=['DELETE'], strict_slashes=False)
def delete_location(id):
    """delete a location based on id"""

    location = storage.get(Location, id)

    if location is None:
        abort(400, description='No location with an id of {}'.format(id))
    
    item_deleted = storage.delete('Location', id)

    if item_deleted is None:
        abort(400, description='location with an id of {} not deleted'.format(id))

    return make_response(json.dumps("location deleted successfully"), 200)




