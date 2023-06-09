#!/usr/bin/python3
from api.v1.views import app_views
from models.prescription import Prescription
from models.drugs import Drugs
from flask import json,jsonify, make_response, request, abort
from models import storage

storage_type = 'fs_storage'

@app_views.route('/prescripting/<presc_id>/drugs/<drug_id>', methods=['POST'], strict_slashes=False)
def create_presc_drug(presc_id, drug_id):
    "link a drug to a prescription"

    if not request.get_json():
        abort(400, description='not a json')

    prescription = storage.get(Prescription, presc_id)

    if prescription is None:
        abort(404, description='prescription not found')
    
    drug = storage.get(Drugs, drug_id)
    if drug is None:
        abort(404, description='drug not found')

    data = request.get_json()
    

    if storage_type == 'fs_storage':
        values = ['price', 'comments', 'side_effects']
        presc = {}
        presc['drug'] = drug_id
        for key, value in data.items():
            if key in values:
                presc[key] = value

        # append to the presciption drugs list
        prescription.drugs.append(presc)
        prescription.save()
        return make_response(jsonify(prescription.to_dict()), 201)
    else:
        #for db_storage
        ...



@app_views.route("/prescripting/<presc_id>/drugs/<drug_id>", methods=['DELETE'], strict_slashes=False)
def delete_presc_drug(presc_id, drug_id):
    """delete a prescripted drug/ remove a drug from prescription"""
    
    prescription = storage.get(Prescription, presc_id)

    if prescription is None:
        abort(400, description='No Prescription with an id of {}'.format(id))
    
    for drug in prescription.to_dict():
        if drug == 'drugs':
            drugs_list = prescription.to_dict()[drug]
            for item in drugs_list:
                if item['drug'] == drug_id:
                    drugs_list.remove(item)
            prescription.to_dict()['drugs'] = drugs_list
            prescription.save()
        return make_response(json.dumps("drug deleted successfully"), 200)
    
    abort(400, description='No drug found'.format(id))
    