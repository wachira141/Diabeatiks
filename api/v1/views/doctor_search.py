#!/usr/bin/python3
from flask import request, jsonify, json
from api.v1.views import app_views
from models.daetician import Daetician
from models import storage
from models.doctor import Doctor



@app_views.route('/search', methods=['GET'], strict_slashes=False)
def search():
    """search for an item with the provided args in query string"""

    storage.all(Doctor)
    

    speciality = request.args.get('speciality', default=None, type=str)
    if speciality:
        filtered_items = storage.filters('speciality', speciality)

    
    facility = request.args.get('facility', default=None, type=str)
    if facility:
        filtered_items = storage.filters('facility', facility)

    
    location = request.args.get('location', default=None, type=str)
    if location:
        filtered_items = storage.filters('location', location)



    subcounty = request.args.get('subcounty', default=None, type=str)
    if subcounty:
        filtered_items = storage.filters('subcounty', subcounty)

    
    county = request.args.get('county', default=None, type=str)
    if county:
        filtered_items = storage.filters('county', county)


  

    return jsonify(  items = {
        "data": filtered_items,
        "item_num":len(filtered_items)
    })
    
"""
all_items
if county
   filter and return
   #problem -> what if i pass another field


"""
    

