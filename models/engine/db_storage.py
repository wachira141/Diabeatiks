from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.patient import Patient
from models.doctor import Doctor
from models.appointments import Appointments
from models.cmhw import CMHW
from models.community import Community
from models.community_members import Community_members
from models.county import County
from models.daetician import Daetician
from models.drugs import Drugs
from models.files import Files
from models.single_file import Single_file
from models.location import Location
from models.marketplace import Market_place
from models.meal import Meal
from models.patient import Patient
from models.pharmacist import Pharmacist
from models.prescription import Prescription
from models.single_file import Single_file
from models.speciality import Speciality
from models.subcounty import Subcounty
from models.userlocation import UserLocation
from models.village import Village
classes = {
    "Doctor":Doctor, 
    "Patient":Patient,
    "Appointments":Appointments,
    "CMHW":CMHW,
    "Community":Community,
    "C_members":Community_members,
    "County":County,
    "Daetician":Daetician,
    "Drugs":Drugs,
    "Files":Files,
    "Single_file":Single_file,
    "Location":Location,
    "MarketPlace":Market_place,
    "Meal":Meal,
    "Patient":Patient,
    "Pharmacist":Pharmacist,
    "Prescription":Prescription,
    "SingleFile":Single_file,
    "Speciality":Speciality,
    "Subcounty":Subcounty,
    "Userlocation":UserLocation,
    "Village":Village
    }



class Db_storage:
    """class to have a direct interaction with MYSQL db"""

    __engine = ''
    __session = ''

    def __init__(self):
        """instantiate the Db_storage class and create an engine"""
        self.__engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
        


    def new(self, obj):
        """add a new object to the session pending state"""
        self.__session.add(obj)

    def save(self):
        """commit the pending object on the database session"""
        self.__session.commit()

    def get(self, cls, id):
        """get an object from the current database session"""
        if cls is None:
            print("please provide a class")
            return 1
        if id is None:
            print("please provide an id")
            return 1
        if cls not in classes:
            print("{} class unknown".format(cls))
            return 1
        obj = self.__session.query(cls)
        return obj

    def all(self, cls=None):
        """get objects from the current database session"""
        items = {}
        for clss in classes:
            if cls is None or clss is cls or classes[clss] is cls:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    items[key] = obj
        return (items)

    def reload(self):
        """reload the database session"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session

    def delete(self, obj=None):
        """delete the object from the database if is not none"""
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """remove the current object from the session"""
        self.__session.remove()