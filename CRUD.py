#Author: Alexandrea Teigeler (Fullwood)
#Date  : LATEST UPDATE ==> 12-05-2022
#About : CRUD application for animal shelter database, used for class CS 340


from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:54504/AAC' % (username, password))
        # where xxxx is your unique port number
        self.database = self.client['AAC']
		
# C in CRUD
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary
            if insert!=0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# R in CRUD. 
    def read(self, criteria=None):
        if criteria:
            data = self.database.animals.find(criteria,{"_id":False})
            print("Search Results:")
            return data
        else:
            data = self.database.animals.find({},{"_id":False})

            return data
        
    def rescue(self, choice):
        if (choice == 1):
            data = self.database.animals.find({"breed":{"$in":["Labrador Retriever Mix",
                                                               "Chesapeake Bay Retriever",
                                                               "Newfoundland"
                                                                  ]},
                                               "sex_upon_outcome":"Intact Female",
                                               "age_upon_outcome_in_weeks":{"$gte":26,"$lte":156}},{"_id":False})
            
        elif (choice == 2):
            data = self.database.animals.find({"breed":{"$in":["German Shepherd",
                                                               "Alaskan Malamute",
                                                               "Old English Sheepdog",
                                                               "Siberian Husky",
                                                               "Rottweiler"
                                                                  ]},
                                               "sex_upon_outcome":"Intact Male",
                                               "age_upon_outcome_in_weeks":{"$gte":26,"$lte":156}},{"_id":False})
            
        elif (choice == 3):
            data = self.database.animals.find({"breed":{"$in":["Doberman Pinscher",
                                                               "German Shepard",
                                                               "Golden Retriever",
                                                               "Bloodhound",
                                                               "Rottwieler"
                                                                  ]},
                                               "sex_upon_outcome":"Intact Male",
                                               "age_upon_outcome_in_weeks":{"$gte":20,"$lte":300}},{"_id":False})    
            
        else:
            data = self.database.animals.find({},{"_id":False})
       
        return data
        
       
			
# U in CRUD, update database data		
    def update(self, id, data_to_change, new_data):
        if data:
            update_result = self.database.animals.update({'_id':id}, {'$set':{data_to_change: new_data}})

# if update is successful...
            if update!=0:
                return update_result
            else:
                return False
        else:
            raise Exception("Nothing to update")

#D in CRUD, delete data in database
    def delete(self, id, data_to_delete):
        if data:
            deleted = self.database.animals.delete_many({id:data_to_delete}) # deletes all matching documents with this ID

# if deletion is successful...
            if delete!=0:
                print(deleted)
            else:
                print("Did not delete")
        else:
            raise Exception("Nothing to delete")

            