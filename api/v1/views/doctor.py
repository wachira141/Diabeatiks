#!/usr/bin/python3
from flask import make_response, request, jsonify, json, abort
from api.v1.views import app_views
from models.doctor import Doctor
from models import storage



@app_views.route('/doctors', methods=['GET'], strict_slashes=False)
def get_doctors():
    """get all doctor's from our storage"""
    doctors = storage.all(Doctor).values()
    items = []

    for obj in doctors:
        items.append(obj.to_dict())
    return make_response(json.dumps(items), 200)

@app_views.route('/doctor/<id>', methods=['GET'], strict_slashes=False)
def get_doctor(id):
    """get a single object of a doctor"""
    doctor = storage.get(Doctor, id)
    if doctor is None:
        return make_response(jsonify("No Doctor with an id of {}".format(id)), 404)
    
    return make_response(json.dumps(doctor.to_dict()), 200)
    

@app_views.route('/doctor', methods=['POST'], strict_slashes=False)
def create_doctor():
    """create a new doctor """
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
        abort(404, description='No doctor with an id of {}'.format(id))
    
    data = request.get_json()

    ignore_keys = ['id', 'created_at', 'updated_at']

    for key, val in data.items():
        if key not in ignore_keys:
            setattr(doctor, key, val)
    storage.save
    return make_response(json.dumps(doctor.to_dict()), 200)
    



@app_views.route('/doctor/<id>', methods=['DELETE'], strict_slashes=False)
def delete_doctor(id):
    """delete a doctor based on id"""

    doctor = storage.get(Doctor, id)

    if doctor is None:
        abort(400, description='No Doctor with an id of {}'.format(id))
    
    item_deleted = storage.delete('Doctor', id)

    if item_deleted is None:
        abort(400, description='Doctor with an id of {} not deleted'.format(id))

    return make_response(json.dumps("doctor deleted successfully"), 200)
    

