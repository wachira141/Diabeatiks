#!/usr/bin/python3
import json
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
import models

classes = {
    "Doctor":Doctor, 
    "Patient":Patient,
    "Appointment":Appointments,
    "CMHW":CMHW,
    "Community":Community,
    "C_members":Community_members,
    "County":County,
    "Daetician":Daetician,
    "Drugs":Drugs,
    "Files":Files,
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

class FileStorage:
    """ Serialize an object to a JSON file and deserialize to an object"""

    __objects = {}
    __file_name = 'file.json'

    # def all(self, obj=None):
    #     """get all saved json objects from filestorage"""
    #     all_obj = {}
    #     if obj is not None:
    #         obj_name = obj.__class__.__name__ 
    #         if obj_name in classes:
    #             with open(self.file_name, 'r')as file:
    #                 objects = json.load(file)
    #             for k, v in objects:
    #                 if obj_name == v.__class__:
    #                     all_obj.append(objects[k])
    #             return all_obj
    #         else:
    #             print("{} is not a class".format(obj.__class__.__name__ ))
    #             return False
    #     else:
    #         return 'all objects'

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, args):
        """create a new object to be serialized to a JSON """
        if args is not None:
            key = args.__class__.__name__ + '.' + args.id
            self.__objects[key] = args
    def save(self):
        """serialize the obj to a json file"""
        json_objs = {}
        for k in self.__objects:
            json_objs[k] = self.__objects[k].to_dict()

        with open(self.__file_name, 'w') as file:
            json.dump(json_objs, file)
    
    def reload(self):
        """deserialize a JSON file to objects"""
        try:
            with open(self.__file_name, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass



    def get(self, cls=None, id=None):
        """get a single object from saved JSON file object"""
        if cls == None:
            print("class cannot be none")
            return None
        if id == None:
            print("id filed should not be none")
            return None
        items = models.storage.all(cls)
        for k, v in items.items():
            if items[k].id == id:
                return v
        return None
        

    def delete(self, cls_name=None, id=None):
        """delete an object saved in the json file"""
        if cls_name is None:
            print("class should not be None")
            return None
        if id is None:
            print("id should not be None")
            return None
        
        
        key = cls_name + '.' + id
       
      
        if key in self.__objects:
            del self.__objects[key]
            models.storage.save()
            return True
            
        
    

    def count(self, cls=None):
        """return the number of our objects"""
        if cls in classes:
            items = models.storage.all(cls).values()
            return len(items)
        elif cls== None:
            return(len(models.storage.all().values()))
        else:
            print("no instance of class {} found".format(cls))
            return None
    
    def close(self):
        """close the current db session"""
        models.storage.reload()


