#!/usr/bin/python3
import cmd
import models, shlex


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




class DBTKCommand(cmd.Cmd):
    """Diabetiks command line program"""
    # intro = 'Diabetiks console'
    prompt = 'diabetiks$ '

    def emptyline(self) -> bool:
        return False
    
    def do_exit(self, arg):
        """type exit to exit the console"""
        return True
    
    def do_EOF(sle, arg):
        """Exit the program"""
        return True

    def do_create(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("**classname missing**")
            return False
        if args[0] in classes:
            kwrgs = {}
            for obj in args[1:]:
                if '=' in obj:
                    #split on '='
                    kvalues = obj.split('=', 1)
                    key = kvalues[0]
                    value = kvalues[1]
                    if value[0] == value[-1] == "'":
                        value = value
                    else:
                        try:
                            value = int(value)
                        except:
                            try:
                                value = float(value)
                            except:
                                pass
                    kwrgs[key] = value
            instance = classes[args[0]](**kwrgs)
            instance.save()
            print(instance.id)
            models.storage.reload()
        else:
            print('No instance of class {} found'.format(args[0]))
            return False
    
    def do_delete(self, arg):
        """delete an object"""
        args = arg.split()
        if len(args) == 0:
            print("**classname missing**")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + '.' + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("no {} with an id of {}".format(args[0], args[1]))
                    return None
            else:
                print('instance id missing')
                return False
        else:
            print('No instance of class {} found'.format(args[0]))
            return False


    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_get(self, arg):
        """get a single class instance"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("Please provide a class name")
            return 1
        if len(args) > 1:
            if args[0] in classes:
                item = models.storage.get(args[0], args[1])
                if item is None:
                    print("No instance of {} with an id of {}".format(args[0], args[1]))
                    return 1
                print(item)
            else:
                print("no instance of {} found".format(args[0]))
                return 1
        else:
            print("please provide an id for the object")
            return 1

    


    def do_count(self, arg):
        """return the num of saved objects"""
        args = shlex.split(arg)
        if len(args )> 0:
            items = models.storage.count(args[0])
            print(items)
        else:
            print(models.storage.count())
            return 0
        

    def do_update(self, arg):
        """update a json object saved in the JSON file"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("**classname missing**")
            return False
        if args[0] in classes:
            kwrgs = {}
            for obj in args[1:]:
               ...
        else:
            print('No instance of class {} found'.format(args[0]))
            return False



    def help_create(self):
        print('Usage <create class [fields]>')


if __name__ == "__main__":
    DBTKCommand().cmdloop()