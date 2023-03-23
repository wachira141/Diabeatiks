#!/usr/bin/python3
from flask import request, jsonify, abort, make_response
from api.v1.views import app_views
from models import storage
from models.files import Files
from models.single_file import Single_file
from models.appointments import Appointments
from models.daetician import Daetician
from models.doctor import Doctor
from models.pharmacist import Pharmacist
from models.patient import Patient

field_list = {
    "daetician":Daetician, 
    "pharmacist":Pharmacist, 
    "doctor":Doctor,
    "patient":Patient
    }


@app_views.route('/user/appointment/<app_id>/files', methods=['POST'], strict_slashes=False)
def create_file(app_id):
    """create a new prescription for a patient"""
    if not request.get_json():
        abort(400, description='Not a json')


    category = request.args.get('category', default=None, type=str)
    if category is None:
        abort(404, description='No category specified')
    


    data = request.get_json()

    if not data['title']:
        abort(400, description='provide the files title')
    #simulate checking user with a cookie
   
    if 'user' not in data:
        """user is the id of the file creator passed through the body"""
        abort(404, description='no user requested')

    authorized_categories = ['doctor', 'daetician', 'pharmacist', 'patient']

    if category not in authorized_categories:
        abort(400, description='Unknown user specified')
    
    file_creator = storage.get(field_list[category], data['user'])
    
    if file_creator is None:
        abort(404, description='No {} found with the id specified'.format(category))

    files = Files(**data)
    files.save()

    appointments = storage.get(Appointments, app_id)
    if appointments is None:
        abort(400, description='Unknown error occurred!')
   
    
    setattr(appointments, 'file_uploads', files.id)
    appointments.save()

    return make_response(jsonify(files.to_dict()), 201)



@app_views.route('/files/<id>', methods=['GET'], strict_slashes=False)
def get_file(id):
    """get a file by an id"""
    file = storage.get(Files, id)
    if file is None:
        abort(400, description='No file with an id of {} found'.format(id))
    

    #get all single files contained in this file
    all_single_files = storage.all(Single_file).values()
    all_files = []
    for s_file in all_single_files:
        if id == s_file.to_dict()['file_id']:
            all_files.append(s_file.to_dict())
    
    return make_response(jsonify(all_files), 200)



@app_views.route('/files/<file_id>', methods=['PUT'], strict_slashes=False)
def update_files(file_id):
    """update a file in the storage"""
    if not request.get_json():
        abort(400, description='please provide a valid json')
    file = storage.get(Files, file_id)
    if file is None:
        abort(404, description='No file with an id of {}'.format(file_id))
    
    data = request.get_json()

    ignore_keys = ['id', 'created_at', 'updated_at', 'approved', 'user', 'sent_to']

    for key, val in data.items():
        if key not in ignore_keys:
            setattr(file, key, val)
    file.save()
    return make_response(jsonify(file.to_dict()), 200)



@app_views.route('/files/<id>', methods=['DELETE'], strict_slashes=False)
def delete_files(id):
    """delete a file by an id"""


    #should loop through all file
    file = storage.get(Files, id)

    if file is None:
        abort(400, description='No file with an id of {}'.format(id))
    
    item_deleted = storage.delete('Files', id)

    if item_deleted is None:
        abort(400, description='Files with an id of {} not deleted'.format(id))

    return make_response(jsonify("files deleted successfully"), 200)








