#!/usr/bin/python3
from api.v1.views import app_views
from models.prescription import Prescription
from models.appointments import Appointments
from models.patient import Patient
from models import storage
from flask import json, jsonify, make_response, request, abort

app_storage = 'fs_storage'



@app_views.route('/user/<id>/prescription', methods=['POST'], strict_slashes=False)
def create_prescription(id):
    """create a new prescription for a patient"""
    if not request.get_json():
        abort(400, description='Not a json')
    data = request.get_json()
    """
    notes-:
         on fs, prescription will have a list of drugs
         on db_storage, presc will have a many to many rlationship with drugs
    """
    if not data['title']:
        abort(400, description='provide the prescription title')
    user = storage.get(Patient, id)
    if user is None:
        abort(404, description='No Patient found')
    
    if app_storage == 'fs_storage':
        data.update({'drugs', []})

    
    new_presc = Prescription(**data)
    
    new_presc.save()
    return make_response(jsonify(new_presc.to_dict()), 200)



@app_views.route('/prescription/<presc_id>/appointment/<app_id>', methods=['PUT'], strict_slashes=False)
def add_presc_to_app(presc_id, app_id):
    """add a prescriptionto an appointment"""
    appointment = storage.get(Appointments, app_id)
    if appointment is None:
        abort(404, description='appointment not found')

    prescription = storage.get(Prescription, presc_id)
    if prescription is None:
        abort(404, description='prescription not found')
    

    setattr(appointment, 'prescription', presc_id)
    appointment.save()
    return make_response(jsonify(appointment.to_dict()), 200)


@app_views.route('/prescription/<id>', methods=['GET'], strict_slashes=False)
def get_presc(id):
    """ get a single prescription"""
    presc = storage.get(Prescription, id)
    if presc is None:
        abort(400, description='prescription not found')
    return make_response(jsonify(presc.to_dict()), 200)

@app_views.route('/user/<user_id>/prescription', methods=['GET'], strict_slashes=False)
def get_prescs(user_id):
    """get user's prescription"""
    user = storage.get(Patient, user_id)
    if user is None:
        abort(404, description='Patient not found')
    prescs = storage.all(Prescription).values()

    user_presc = []
    for psc in prescs:
        if psc.to_dict()['user_id'] == user_id:
            user_presc.append(psc.to_dict())

    return make_response(jsonify(user_presc),200)


@app_views.route('/prescription/<presc_id>', methods=['PUT'], strict_slashes=False)
def update_presc_update(presc_id):
    """update prescription's details"""
    if not request.get_json():
        abort(400, description='please provide a valid json')
    prescription = storage.get(Prescription, presc_id)
    if prescription is None:
        abort(404, description='No Prescription with an id of {}'.format(id))
    
    data = request.get_json()

    ignore_keys = ['id', 'created_at', 'updated_at']

    for key, val in data.items():
        if key not in ignore_keys:
            setattr(prescription, key, val)
    prescription.save
    return make_response(json.dumps(prescription.to_dict()), 200)
    

@app_views.route('/prescription/<id>', methods=['DELETE'], strict_slashes=False)
def delete_presc(id):
    """delete a prescription object from our storage"""
    prsc = storage.get(Prescription, id)
    if prsc is None:
        abort(404, description='prescription not found')
    
    deleted_presc = storage.delete('Prescription', id)
    if delete_presc is None:
        abort(404, description='prescription not found')
    
    return make_response(jsonify('Prescription deleted successfully!'), 200)