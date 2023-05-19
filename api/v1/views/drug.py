#!/usr/bin/python3
from api.v1.views import app_views
from models.drugs import Drugs
from flask import json,jsonify, make_response, request, abort
from models import storage

# all_drugs = storage.all(Drugs).values()

@app_views.route('/drug', methods=['POST'], strict_slashes=False)
def create_drug():
    """create a drug object"""
    if not request.get_json():
        abort(400, description='Not a valid json')
    
    data = request.get_json()

    #check if drug already in the storage by ['name', 'd_group', 'age', 'condition']
    # this is to eliminate adding same drug twice
    all_drugs = storage.all(Drugs).values()
    for drg in all_drugs:
        print(drg)
        if drg.to_dict()['name'] == data['name']:
            if drg.to_dict()['d_group'] == data['d_group']:
                if drg.to_dict()['age'] == data['age']:
                    if drg.to_dict()['condition'] == data['condition']:
                        abort(400, description='drug already added')


    drug = Drugs(**data)
    drug.save()
    return make_response(jsonify(drug.to_dict()), 201)


@app_views.route('/drugs', methods=['GET'], strict_slashes=False)
def get_all_drugs():
    """get all drugs from our storage"""
    all_drugs = storage.all(Drugs).values()

    all = [drug.to_dict() for drug in all_drugs]
    return make_response(jsonify(all), 200)


@app_views.route('/drug/<id>', methods=['GET'], strict_slashes=False)
def get_drug(id):
    """get a drug by id"""
    drug = storage.get(Drugs, id)

    if drug is None:
        abort(404, description='No drug with an id of {} found'.format(id))
    
    return make_response(jsonify(drug.to_dict()), 200)

@app_views.route('/drug/<id>', methods=['PUT'], strict_slashes=False)
def update_drug(id):
    """update  a drug obj in storage"""
    if not request.get_json():
        abort(400, description='not a valid json')

    drug = storage.get(Drugs, id)

    if drug is None:
        abort(404, description='No drug with an id of {} found'.format(id))
    
    ignore_keys = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    
    for k, v in data.items():
        if k not in ignore_keys:
            setattr(drug, k, v)
    storage.save()
    return make_response(jsonify(drug.to_dict()), 200)


@app_views.route('/drug/<id>', methods=['DELETE'], strict_slashes=False)
def delete_drug(id):
    """delete a drug from our storage"""
    drug = storage.get(Drugs, id)
    if drug is None:
        abort(404, description='Drug not found')
    
    drug_dlt = storage.delete('Drugs', id)
    if drug_dlt is None:
        abort(400, description='Drug {} not deleted'.format(id))
    return make_response(jsonify('Drug deleted successfully'), 200)