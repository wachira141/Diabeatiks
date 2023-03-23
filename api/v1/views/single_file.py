#!/usr/bin/python3
from flask import request, abort, make_response, jsonify
from api.v1.views import app_views
from models.single_file import Single_file
from models.files import Files
from models import storage

app_storage ='fs_storage'



@app_views.route('/single-files/<file_id>/single_file', methods=['POST'], strict_slashes=False)
def create_s_file(file_id):
    """create a single file and link a singlefile to related files"""
    if not request.get_json():
        abort(400, description='not a valid json')
    
    main_file = storage.get(Files, file_id)
    if main_file is None:
        abort(404, description='file does not exist')

    data = request.get_json()
    data['file_id'] = file_id
    if 'name' not in data:
        abort(400, description='provide the files name')

    # if app_storage == 'fs_storage':
       

    file = Single_file(**data)
    file.save()
    return make_response(jsonify(file.to_dict()), 200)


@app_views.route('/single_file/<id>', methods=['GET'], strict_slashes=False)
def get_single_f(id):
    """get a file from our storage"""
    file = storage.get(Single_file, id)

    if file is None:
        abort(404, description='No file with an id of {} found'.format(id))
    
    return make_response(jsonify(file.to_dict()), 200)


@app_views.route('/edit/<id>', methods=['PUT'], strict_slashes=False)
def update_file(id):
    """update  a file obj in storage"""
    if not request.get_json():
        abort(400, description='not a valid json')
    s_file = storage.get(Single_file, id)
    data = request.get_json()

    if s_file is None:
        abort(404, description='No file with an id of {} found'.format(id))
    
    ignore_keys = ['id', 'created_at', 'updated_at', 'file_id']

    for k, v in data.items():
        if k not in ignore_keys:
            setattr(s_file, k, v)
    storage.save()
    return make_response(jsonify(s_file.to_dict()), 200)


@app_views.route('/file-remove/<id>', methods=['DELETE'], strict_slashes=False)
def delete_file(id):
    """delete a file from our storage"""
    s_file = storage.get(Single_file, id)
    if s_file is None:
        abort(404, description='file not found')
    
    file_dlt = storage.delete('Single_file', id)
    if file_dlt is None:
        abort(400, description='file {} not deleted'.format(id))
    return make_response(jsonify('file deleted successfully'), 200)