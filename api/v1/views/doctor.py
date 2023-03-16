#!/usr/bin/python3
from flask import make_response, request, jsonify, json, abort
from api.v1.views import app_views
from models.doctor import Doctor
from models import storage



@app_views.route('/doctors', methods=['GET'], strict_slashes=False)
def get_doctor():
    """get all doctor's from our storage"""
    doctors = storage.all(Doctor)
    items = []

    for obj in doctors:
        items.append(obj.to_dict())
    return json.dumps(items)

@app_views.route('/doctor/<id>', methods=['GET'], strict_slashes=False)
def get_doctor(id):
    """get a single object of a doctor"""
    doctor = storage.get(Doctor, id)
    if doctor is None:
        return make_response(jsonify("No Patient with an id of {}".format(id)))
    return json.dumps(doctor.to_dict(), 200)
    

@app_views.route('/doctor', methods=['POST'], strict_slashes=False)
def create_doctor():
    """create a new doctor """
    if not request.get_json():
        abort(400, description='please provide a valid json format')
    if 'f_name' or 'l_name' not in request.get_json():
        abort(400, description='please provide all names')
    
    if 'email' not in request.get_json():
        abort(400, description='email is not provided')
    # check the email format
    data = request.get_json()
    new_doctor = Doctor(**data)
    new_doctor.save()

    return make_response(json.dumps(new_doctor.to_dict()), 201)

  

@app_views.route('/doctor/<id>', methods=['PUT'], strict_slashes=False)
def update_doctor(id):
    """update doctor's details"""
    if not request.get_json():
        abort(400, description='please provide a valid json')
    doctor = storage.get(Doctor, id)
    if doctor is None:
        abort(400, description='No patient with an id of {}'.format(id))
    
    data = request.get_json()
    for key, val in doctor:
        if key is not 'id' or key is not 'created_at' or key is not 'updated_at':
            setattr(data, key, val)
    return make_response(json.dumps(data.to_dict()), 200)
    



@app_views.route('/patient/<id>', methods=['DELETE'], strict_slashes=False)
def  delete_doctor(id):
    """delete a doctor based on id"""
    if not request.get_json():
        abort(400, description='please provide a valid json')

    doctor = storage.get(Doctor, id)

    if doctor is None:
        abort(400, description='No patient with an id of {}'.format(id))
    
    storage.delete(Doctor, id)

