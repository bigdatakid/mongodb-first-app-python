import pymongo
import pprint
import os

MongoDB_cluster_password = os.environ["MONGODB_CLUSTER_PASSWORD_ENV"]
MongoDB_cluster_name = os.environ["MONGODB_CLUSTER_NAME_ENV"]
MongoDB_user_name = "mongodba"

from pymongo.errors import ConnectionFailure

connectionString = "mongodb+srv://" + MongoDB_user_name + ":" + MongoDB_cluster_password  + "@" + MongoDB_cluster_name
connectionString= connectionString + "/test?retryWrites=true"

print(connectionString)

# replace <PASSWORD> with user password
client = pymongo.MongoClient()

#Selecting  a database
blogDatabase = client.blog

# Selecting a collection
usersCollection = blogDatabase.users

rocha = {
    "username": "rocha",
    "password": "password",
    "lang": "EN"
}

usersCollection.insert_one(rocha)

user = usersCollection.find_one()

print(user)