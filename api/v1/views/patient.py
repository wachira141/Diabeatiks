#!/usr/bin/python3
from api.v1.views import app_views
from flask import make_response, jsonify,json, request, abort
from models import storage
from models.patient import Patient

# @app_views.route('/patient', methods=['GET'], strict_slashes=False)
# def status():
#     return make_response(json.dumps("Status:Success"), 200)


@app_views.route('/patient', methods=['GET'], strict_slashes=False)
def get_patients():
    """get all patients from our storage"""
    patients = storage.all(Patient)
    items = []

    for obj in patients:
        items.append(obj.to_dict())
    return json.dumps(items)

@app_views.route('/patient/<id>', methods=['GET'], strict_slashes=False)
def get_patient(id):
    """get a single object of a patient"""
    patient = storage.get(Patient, id)
    if patient is None:
        return make_response(jsonify("No Patient with an id of {}".format(id)))
    return json.dumps(patient.to_dict(), 200)
    

@app_views.route('/patient', methods=['POST'], strict_slashes=False)
def create_patient():
    """create a new patient """
    if not request.get_json():
        abort(400, description='please provide a valid json format')
    if 'f_name' or 'l_name' not in request.get_json():
        abort(400, description='please provide all names')
    
    if 'email' not in request.get_json():
        abort(400, description='email is not provided')
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
        abort(400, description='No patient with an id of {}'.format(id))
    
    data = request.get_json()
    for key, val in patient:
        if key is not 'id' or key is not 'created_at' or key is not 'updated_at':
            setattr(data, key, val)
    return make_response(json.dumps(data.to_dict()), 200)
    



@app_views.route('/patient/<id>', methods=['DELETE'], strict_slashes=False)
def  delete_patient(id):
    """delete a patient based on id"""
    if not request.get_json():
        abort(400, description='please provide a valid json')

    patient = storage.get(Patient, id)

    if patient is None:
        abort(400, description='No patient with an id of {}'.format(id))
    
    storage.delete(Patient, id)

