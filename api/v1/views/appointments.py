#!/usr/bin/python3
from flask import make_response, json, jsonify, request, abort
from api.v1.views import app_views
from models.appointments import Appointments
from models.doctor import Doctor
from models.daetician import Daetician
from models.pharmacist import Pharmacist
from models.patient import Patient
from models import storage

appointers_list = {
    "daetician":Daetician, 
    "pharmacist":Pharmacist, 
    "doctor":Doctor,
    }



@app_views.route('/appointments', methods=['POST'], strict_slashes=False)
def create_appointments():
    """create an appointment"""
    if not request.get_json():
        abort(400, description='not a valid json')

    category = request.args.get('category', default=None, type=str)
   
    if category is None:
        abort(404, description='No category specified')
    
    # get the appointer's id from the url query string
    appointer_id = request.args.get('appointer', default=None, type=str)
    if appointer_id is None:
        abort(404, description='No appointer specified')

    
    data = request.get_json()

    # find if the user is same with the appointers id from query string
    if data['user'] == appointer_id:
        abort(400, description='You cannot make an appointment with yourself')

    if 'user' not in data:
        abort(404, description='no user requested')

    
    # user = storage.get(Patient, data['user'])

    # if user is None:
    #     abort(404, description='user not found')

    
    authorized_categories = ['doctor', 'daetician', 'pharmacist']


    # check if category is only from accepted
    if category not in authorized_categories:
        abort(400, description='Unknown user specified')
    
    get_appointer = storage.get(appointers_list[category], appointer_id)

    if get_appointer is None:
        abort(404, description='No {} found with the id specified'.format(category))
    
    appnt_id = get_appointer.to_dict()['id']

    data['appointer_id'] = appnt_id
    data['category'] = category
    data['approved'] = False
    
    appontment = Appointments(**data)
    appontment.save()
    
    return make_response(jsonify(appontment.to_dict()), 201)



@app_views.route('/appointments/<id>', methods=['GET'], strict_slashes=False)
def get_appointment(id):
    """get an appointment by an id"""
    appointment = storage.get(Appointments, id)
    if appointment is None:
        abort(400, description='No appointment with an id of {} found'.format(id))
    return make_response(jsonify(appointment.to_dict()), 200)


@app_views.route('/user/<user_id>/appointments', methods=['GET'], strict_slashes=False)
def get_appntmnts(user_id):
    """get all user's appointments [get all appointments i have sent]"""
    user = storage.get(Patient, user_id)
    if user is None:
        abort(404, description='user not found')
    appointments = storage.all(Appointments).values()

    user_appntmnts = []
    for apnt in appointments :
        if apnt.to_dict()['user'] == user_id:
            user_appntmnts.append(apnt.to_dict())

    return make_response(jsonify(user_appntmnts),200)



@app_views.route('/appointment/<appnt_id>', methods=['PUT'], strict_slashes=False)
def update_appointment(appnt_id):
    """update an appointment created"""
    if not request.get_json():
        abort(400, description='please provide a valid json')

    # check if the appointment exists
    appointment = storage.get(Appointments, appnt_id)
    if appointment is None:
        abort(404, description='No appointment with an id of {}'.format(appnt_id))
    
    data = request.get_json()

    ignore_keys = ['id', 'created_at', 'updated_at', 'approved', 'user_id ']

    for key, val in data.items():
        if key not in ignore_keys:
            setattr(appointment, key, val)
    appointment.save()
    return make_response(jsonify(appointment.to_dict()), 200)




@app_views.route('/appointment/<id>', methods=['DELETE'], strict_slashes=False)
def delete_appointment(id):
    """delete an appointment by an id"""
    appointment = storage.get(Appointments, id)

    if appointment is None:
        abort(400, description='No appointment with an id of {}'.format(id))
    
    item_deleted = storage.delete('Appointments', id)

    if item_deleted is None:
        abort(400, description='Appointment with an id of {} not deleted'.format(id))

    return make_response(json.dumps("appointment deleted successfully"), 200)



@app_views.route('/appointments', methods=['GET'], strict_slashes=False)
def get_appointers_appntmnts():
    """get appntmnts sent to a doctor. [get appointments sent to me]"""
    
    # get the appointer's id from the url query string
    appointer_id = request.args.get('appointer', default=None, type=str)
    if appointer_id is None:
        abort(404, description='No appointer specified')
    
    # get the appointments category eg ?category=doctor from query string
    category = request.args.get('category', default=None, type=str)
    if category is None:
        abort(404, description='No category specified')

    # check if the  category is one of the authorized [this is to eliminate sending appointments to eg patients ]
    get_appointer = storage.get(appointers_list[category], appointer_id)

    if get_appointer is None:
        abort(404, description='No {} found with the id specified'.format(category))


    all_appointment = storage.all(Appointments).values()
    if all_appointment is None:
        abort(400, description='No appointments found')

    my_appntmnts = []
    # get all appointments and filter against appointer_id from query string
    for appntmnt in all_appointment:
        if appntmnt.to_dict()['appointer_id'] == appointer_id:
            my_appntmnts.append(appntmnt.to_dict())
    return make_response(jsonify(my_appntmnts), 200)