#!/usr/bin/python3
from flask import make_response, request, jsonify, json, abort
from api.v1.views import app_views
from models.county import County
from models.subcounty import Subcounty
from models import storage



@app_views.route('/county/<county_id>/subcounty', methods=['POST'], strict_slashes=False)
def create_subcounty(county_id):
    """create a county object"""
    if not request.get_json():
        abort(400, descriptions='please provide a valid json')
    
    data = request.get_json()

   
    # counties = storage.all(County).values()
    # county_id = None
    # for obj in counties:
    #     if obj.to_dict()['id'] == data.get('county'):
    #         county_id = obj.to_dict()['id']

 # check if county exists
    county = storage.get(County, county_id)
    if county is None:
        return abort(404, description='no county with an id of {}'.format(county_id))

    
    new_sub_county = Subcounty(**data)
    new_sub_county.county = county.to_dict()['id']
    new_sub_county.save()

    return make_response(json.dumps(new_sub_county.to_dict()), 201)


@app_views.route('/subcounty/<id>', methods=['GET'], strict_slashes=False)
def get_subcounty(id):
    """get a subcounty by id"""
    subcounty= storage.get(Subcounty, id)
    
    if subcounty is None:
        abort(400, description='No subcounty found')
    return make_response(json.dumps(subcounty.to_dict()), 200)




@app_views.route('/county/<county_id>/subcounties', methods=['GET'], strict_slashes=False)
def get_all_subcounties(county_id):
    """get all subcounties in a county referenced by an county_id"""
    county = storage.get(County, county_id)

    if county is None:
        abort(404, description='county not found')
    
    subcounties = storage.all(Subcounty).values()
    sc_list = []
    for sbcnty in subcounties:
        if sbcnty.to_dict()['county'] == county_id:
            sc_list.append(sbcnty.to_dict())

    return make_response(json.dumps(sc_list), 200)




@app_views.route('/subcounty/<id>', methods=['PUT'], strict_slashes=False)
def update_subcounty(id):
    """update subcounty's details"""
    if not request.get_json():
        abort(400, description='please provide a valid json')
    subcounty = storage.get(Subcounty, id)
    if subcounty is None:
        abort(400, description='No subcounty with an id of {}'.format(id))
    
    data = request.get_json()
    ignore_keys = ['county','created_at', 'updated_at', 'id']

    for key, val in data.items():
        if val not in ignore_keys:
            setattr(subcounty, key, val)
    storage.save()
    return make_response(json.dumps(subcounty.to_dict()), 200)


@app_views.route('/subcounty/<id>', methods=['DELETE'], strict_slashes=False)
def delete_subcounty(id):
    """delete a subcounty based on id"""

    subcounty = storage.get(Subcounty, id)

    if subcounty is None:
        abort(400, description='No subcounty with an id of {}'.format(id))
    
    item_deleted = storage.delete('Subcounty', id)

    if item_deleted is None:
        abort(400, description='subcounty with an id of {} not deleted'.format(id))

    return make_response(json.dumps("Subcounty deleted successfully"), 200)




