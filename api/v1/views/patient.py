#!/usr/bin/python3
from api.v1.views import app_views
from flask import make_response, jsonify,json, request, abort
from models import storage
from models.patient import Patient


@app_views.route('/patient', methods=['GET'], strict_slashes=False)
def get_patients():
    """get all patients from our storage"""
    patients = storage.all(Patient).values()
    items = []

    for obj in patients:
        items.append(obj.to_dict())
    return make_response(json.dumps(items), 200)


@app_views.route('/patient/<id>', methods=['GET'], strict_slashes=False)
def get_patient(id):
    """get a single object of a patient"""
    patient = storage.get(Patient, id)
    if patient is None:
        return make_response(jsonify("No Patient with an id of {}".format(id)), 404)
    return make_response(json.dumps(patient.to_dict()), 200)
    

@app_views.route('/patient', methods=['POST'], strict_slashes=False)
def create_patient():
    """create a new patient """
    if not request.get_json():
        abort(400, description='please provide a valid json format')

    required_details = ['f_name', 'l_name', 'email']

    for detail in required_details:
        if detail not in request.get_json():
            abort(400, description='please provide {}'.format(detail))

    # check the email format
    data = request.get_json()
    new_patient = Patient(**data)
    new_patient.save()

    return make_response(json.dumps(new_patient.to_dict()), 201)

  

@app_views.route('/patient/<id>', methods=['PUT'], strict_slashes=False)
def update_patient(id):
    """update patients details"""
    if not request.get_json():
        abort(400, description='please provide a valid json')
    patient = storage.get(Patient, id)
    if patient is None:
        abort(404, description='No patient with an id of {}'.format(id))
    
    data = request.get_json()
    ignore_keys = ['id', 'created_at', 'updated_at']

    for key, val in data.items():
        if key not in ignore_keys:
            setattr(patient, key, val)
    storage.save
    return make_response(json.dumps(patient.to_dict()), 200)
    
    



@app_views.route('/patient/<id>', methods=['DELETE'], strict_slashes=False)
def  delete_patient(id):
    """delete a patient based on id"""
    patient = storage.get(Patient, id)

    if patient is None:
        abort(400, description='No patient with an id of {}'.format(id))
    
    item_deleted = storage.delete('Patient', id)
    if item_deleted is None:
        abort(400, description='Patient with an id of {} not deleted'.format(id))

    return make_response(json.dumps("Patient deleted successfully"), 200)

