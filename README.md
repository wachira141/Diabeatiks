<h1>Diabetiks</h1>

<p>Diabeatiks is a program that tries to link diabetes patients to all parties involved. it will try
to narrow down the process of finding information and centralize all the needs of a patient to a single site.
Patients will be able to share information with others which include displaying their prescriptions, how they feel about the prescription, physical excercises, meal plans, make appointments and eventually plan for a community hangout. they will also be able to request for reviews about their physical execercise, diet and prescription from the party with the proffessional knowledge on the field required</p>




<h1><b>Usage with curl</b></h1>
<h2>Patient</h2>
<h3>Create a Patient</h3>
<p>curl -X POST -H "Content-Type:application/json" -d'{"f_name":"wilson", "l_name":"wachira", "email":"wachiraw424@gmail.com"}' http://127.0.0.1:5000/api/v1/patient
</p>
<h3>Get a single patient by id</h3>
<p>curl http://127.0.0.1:5000/api/v1/patient/id</p>
<h3>Get all patients</h3>
<p>curl http://127.0.0.1:5000/api/v1/patient</p>
<h3>Update a Patient</h3>
<p>curl -X PUT -H "Content-Type:application/json" -d'{"f_name":"wilson", "l_name":"wachira", "email":"wachiraw424@gmail.com"}' "http://127.0.0.1:5000/api/v1/patient/id"</p>
<h3>Delete Patient</h3>
<p>curl -X DELETE http://127.0.0.1:5000/api/v1/patient/f6e20b1f-222a-43bb-8147-5a7750efd008</p>
<br/>
<br/>
<br/>
<h2>Doctor</h2>
<h3>Create a Doctor</h3>
<p>curl -X POST -H "Content-Type:application/json" -d'{"f_name":"wilson", "l_name":"wachira", "email":"wachiraw424@gmail.com"}' http://127.0.0.1:5000/api/v1/doctor
</p>
<h3>Get a single doctor by id</h3>
<p>curl http://127.0.0.1:5000/api/v1/doctor/id</p>
<h3>Get all doctors</h3>
<p>curl http://127.0.0.1:5000/api/v1/doctor</p>
<h3>Update a Doctor</h3>
<p>curl -X PUT -H "Content-Type:application/json" -d'{"f_name":"wilson", "l_name":"wachira", "email":"wachiraw424@gmail.com"}' "http://127.0.0.1:5000/api/v1/doctor/id"</p>
<h3>Delete Doctor</h3>
<p>curl -X DELETE http://127.0.0.1:5000/api/v1/doctor/id</p>
<br/>
<br/>
<br/>
<h2>Daetician</h2>
<h3>Create a Daetician</h3>
<p>curl -X POST -H "Content-Type:application/json" -d'{"f_name":"wilson", "l_name":"wachira", "email":"wachiraw424@gmail.com"}' http://127.0.0.1:5000/api/v1/daetician
</p>
<h3>Get a single daetician by id</h3>
<p>curl http://127.0.0.1:5000/api/v1/daetician/id</p>
<h3>Get all daetician</h3>
<p>curl http://127.0.0.1:5000/api/v1/daetician</p>
<h3>Update a Daetician</h3>
<p>curl -X PUT -H "Content-Type:application/json" -d'{"f_name":"wilson", "l_name":"wachira", "email":"wachiraw424@gmail.com"}' "http://127.0.0.1:5000/api/v1/daetician/id"</p>
<h3>Delete Daetician</h3>
<p>curl -X DELETE http://127.0.0.1:5000/api/v1/daetician/id</p>
<br/>
<br/>
<br/>
<h2>County</h2>
<h3>Create a County</h3>
<p>curl -X POST -H "Content-Type:application/json" -d'{"name":"Nyeri"}' http://127.0.0.1:5000/api/v1/county
</p>
<h3>Get a single County by id</h3>
<p>curl http://127.0.0.1:5000/api/v1/county/id</p>
<h3>Get all County</h3>
<p>curl http://127.0.0.1:5000/api/v1/county</p>
<h3>Update a County</h3>
<p>curl -X PUT -H "Content-Type:application/json" -d'{"name":"Nairobi"}' "http://127.0.0.1:5000/api/v1/county/id"</p>
<h3>Delete County</h3>
<p>curl -X DELETE http://127.0.0.1:5000/api/v1/county/id</p>
<br/>
<br/>
<br/>
<h2>SubCounty</h2>
<h3>Create a SubCounty</h3>
<p>curl -X POST -H "Content-Type:application/json" -d'{"name":"Kieni West"}' http://127.0.0.1:5000/api/v1/county_id/subcounty
</p>
<h3>Get a single SubCounty by id</h3>
<p>curl http://127.0.0.1:5000/api/v1/subcounty/id</p>
<h3>Get all SubCounty</h3>
<p>curl http://127.0.0.1:5000/api/v1/subcounty</p>
<h3>Update a SubCounty</h3>
<p>curl -X PUT -H "Content-Type:application/json" -d'{"name":"Kasarani"}' "http://127.0.0.1:5000/api/v1/subcounty/id"</p>
<h3>Delete SubCounty</h3>
<p>curl -X DELETE http://127.0.0.1:5000/api/v1/subcounty/id</p>
<br/>
<br/>
<br/>
<h2>Location</h2>
<h3>Create a Location</h3>
<p>curl -X POST -H "Content-Type:application/json" -d'{"name":"Endarasha"}' http://127.0.0.1:5000/api/v1/subcounty/subcounty_id/location
</p>
<h3>Get a single Location by id</h3>
<p>curl http://127.0.0.1:5000/api/v1/location/id</p>
<h3>Get all Locations</h3>
<p>curl http://127.0.0.1:5000/api/v1/subcounty/subcounty_id/location</p>
<h3>Update a Location</h3>
<p>curl -X PUT -H "Content-Type:application/json" -d'{"name":"Kasarani"}' "http://127.0.0.1:5000/api/v1/location/id"</p>
<h3>Delete Location</h3>
<p>curl -X DELETE http://127.0.0.1:5000/api/v1/location/id</p>
<br/>
<br/>
<br/>
<h2>Prescription</h2>
<h3>Create a Prescription</h3>
<p>curl -X POST -H "Content-Type:application/json" -d'{"name":"Endarasha"}' http://127.0.0.1:5000/api/v1/user/user_id/prescription
</p>
<h3>add a prescription to an appointment</h3>
<p>curl -X PUT http://127.0.0.1:5000/api/v1/prescription/prescription_id/appointment/appointment_id'
</p>

<h3>Get a single Prescription by id</h3>
<p>curl http://127.0.0.1:5000/api/v1/prescription/id</p>
<h3>Get all prescriptions</h3>
<p>curl http://127.0.0.1:5000/api/v1/user/user_id/prescription</p>
<h3>Update a Prescription</h3>
<p>curl -X POST -H "Content-Type:application/json" -d'{"description":"This is an updated description about the prescription"}' "http://127.0.0.1:5000/api/v1/prescription/prescription_id"</p>
<h3>Delete Prescription</h3>
<p>curl -X DELETE http://127.0.0.1:5000/api/v1/prescription/prescription_id</p>
<br/>
<br/>
<br/>
<h2>Appointments</h2>
<h3>Create a Appointments</h3>
<p>curl -X POST -H "Content-Type:application/json" -d'{"title":"Renal clinic"}' http://127.0.0.1:5000/api/v1/appointments
</p>
<h3>Get a single appointment by id</h3>
<p>curl http://127.0.0.1:5000/api/v1/appointments/id</p>

<h3>Get user's Appointments</h3>
<p>curl http://127.0.0.1:5000/api/v1/user/user_id/appointments</p>
<h3>Update an Appointment</h3>
<p>curl -X PUT -H "Content-Type:application/json" -d'{"title":"new title"}' "http://127.0.0.1:5000/api/v1/appointment/appointment_id"</p>
<h3>Delete Appointment</h3>
<p>curl -X DELETE http://127.0.0.1:5000/api/v1/appointment/appointment_id</p>
<h3>Get appointments sent to a certain Doctor</h3>
<p>curl http://127.0.0.1:5000/api/v1/appointments?appointer=appointer_id&category=user_category</p>
<span>Please Note: user_category are eg doctor, patient, pharmacist, daetician</span>
<br/>
<br/>
<br/>
<h2>File</h2>
<h3>Create a Appointments</h3>
<p>curl -X POST -H "Content-Type:application/json" -d'{"title":"X-ray"}' http://127.0.0.1:5000/api/v1/user/appointment/appointment_id/files?category=user_category
</p>
<h3>Get a file by id</h3>
<p>curl http://127.0.0.1:5000/api/v1/files/id</p>

<h3>Update a file</h3>
<p>curl -X PUT -H "Content-Type:application/json" -d'{"title":"new title"}' "http://127.0.0.1:5000/api/v1/files/file_id"</p>
<h3>Delete a file</h3>
<p>curl -X DELETE http://127.0.0.1:5000/api/v1/files/file_id</p>
<span>Please Note: user_category are eg doctor, patient, pharmacist, daetician</span>
<br/>
<br/>
<br/>
<h2>Single file</h2>
<h3>Single File</h3>
<p>curl -X POST -H "Content-Type:application/json" -d'{"f_name":"wilson", "l_name":"wachira", "email":"wachiraw424@gmail.com"}' http://127.0.0.1:5000/api/v1/single-files/parentfile_id/single_file
</p>
<h3>Get a single file</h3>
<p>curl http://127.0.0.1:5000/api/v1/single_file/id</p>
<h3>Update a single file</h3>
<h3>Delete a single file</h3>
<p>curl -X DELETE http://127.0.0.1:5000/api/v1/file-remove/id</p>
<br/>
<br/>
<br/>
<h2>Drug</h2>
<h3>Create a Drug</h3>
<p>curl -X POST -H "Content-Type:application/json" -d'{"name":"insulin","category":"heterogeneous", "d_group":"plasis", "age":35, "dosage":"4ml", "frequency":"2ml/12hrs", "condition":"diabetes 2", "known_side_effects":"abit of nausea and mild headache"}' http://127.0.0.1:5000/api/v1/drug
</p>
<h3>Get a single drug</h3>
<p>curl http://127.0.0.1:5000/api/v1/drug/id</p>
<h3>Get all drugs</h3>
<p>curl http://127.0.0.1:5000/api/v1/drugs</p>
<h3>Update a Drug</h3>
<p>curl -X PUT -H "Content-Type:application/json" -d'{"name":"amoxyl", "d_group":"painkillers"}' "http://127.0.0.1:5000/api/v1/drug/id"</p>
<h3>Delete Drug</h3>
<p>curl -X DELETE http://127.0.0.1:5000/api/v1/drug/id</p>

<h1><b>console Usage</b></h1>

localhost PORTFOLIO$./console.py <br/>
* diabetiks$ create Patient f_name="wilson" l_name=wachira age=26 email=wachiraw424@gmail.com<br/>
* diabetiks$ create County name=Nairobi<br/>
* diabetiks$ delete Patient 181a7901-3a45-4382-9931-1e08b80f06df<br/>
* diabetiks$ delete Drug 88c95225-6359-4d43-b990-b885fe5e7d3b<br/>
*diabetiks$ all Prescriptions<br/>
* diabetiks$ all <br/>
* diabetiks$ get Drug 88c95225-6359-4d43-b990-b885fe5e72d6<br/>
* diabetiks$ count Prescription<br/>
* diabetiks$ count <br/>
* diabetiks$ update Pharmacist 88c95225-6359-4d43-b990-b885fe5q45g7<br/>
<p>show usage of help</p>

* diabetiks$ help Classname<br/>


## Installation
* Clone this repository: `git clone https://github.com/wachira141/Diabeatiks`
* Access Diabeatiks directory: `cd Diabetiks`
* Run diabetiks(interactively): `./console <command>`
* Run diabetiks(non-interactively): `echo "<command>" | ./console.py`




#### `models/` directory contains classes used for this project:
[base_model.py](/models/base_model.py) The BaseModel class from which other models will inherit from.

### methods in Basemodel
* `def __init__(self, *args, **kwargs)` - initialize a base model
* `def  save(self)` - persist/save the obj in fs/db and update the updated_at attribute
* `def to_dict(self)` - return a dict representation of all the key value pairs of our object
* `def __str__(self)` - returns the string representation of our object
* `def delete(self)` - delete the current instance from the db

classes inheriting from BaseModel
* [registrant](/models/registrant.py)
* [community_members](/models/community_members.py)
* [community](/models/community.py)
* [appointments](/models/appointments.py)
* [county](/models/county.py)
* [subcounty](/models/subcounty.py)
* [location](/models/location.py)
* [village](/models/village.py)
* [daetician](/models//daetician.py)
* [drugs](/models/drugs.py)
* [file](/models//file.py)
* [files](/models/files.py)
* [location](/models/location.py)
* [marketplace](/models/marketplace.py)
* [meal](/models/meal.py)
* [prescription](/models/prescription.py)
* [single_file](/models/single_file.py)
* [speciality](/models/speciality.py)
* [userlocation](/models/userlocation.py)

classes inheriting from Registrant model
* [patient](/models/patient.py)
* [doctor](/models/doctor.py)
* [pharmacist](/models/pharmacist.py)
* [daetician](/models/daetician.py)
* [community health worker](/models/cmhw.py)

#### `/model/engine` directory contains FileStorage class that handles all the Json serialization and deserialization :
* [filestorage.py](/models/engine/filestorage.py) - serializes instances to a JSON file & deserializes back to instances
* `def all(self, cls=None)` - returns the dictionary __objects
* `def new(self, args)` - create a new object to be serialized to a JSON 
* `def save(self)` - serialize the obj to a json file and saves it to a file.json
* `def reload(self)` - deserializes a JSON file to objects
* `def get(self, cls=None, id=None)` - get a single object from saved Json file by classname and id number
* `def delete(self, class_name=None, id=None)` - delete a single object from file.json by classname and id number
* `def count(self, cls=None)` - return the number count of our objects
* `def close(self)` - close the current db session


## Authors
* Wilson Muriuki - [Github](https://github.com/wachira141) / [Twitter](https://twitter.com/wachira_wilson1) / [email](wachiraw75@gmail.com)
* Jackson Mobe Maina - [Github](https://github.com/swaga32) / [Twitter](https://twitter.com/swaga) / [email](jacksonmbirui@gmail.com)

## License
No copy write protection but the use of any material from this project, please make sure you give credits to the original authors