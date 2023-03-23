#!/usr/bin/python3
from flask import Blueprint

app_views = Blueprint("app_views",__name__, url_prefix="/api/v1/")
from api.v1.views.patient import *
from api.v1.views.doctor import *
from api.v1.views.daetician import *
from api.v1.views.county import *
from api.v1.views.subcounty import *
from api.v1.views.locations import *
from api.v1.views.drug import *
from api.v1.views.prescription import *
from api.v1.views.prescription_drug import *
from api.v1.views.appointments import *
from api.v1.views.files import *
from api.v1.views.single_file import *