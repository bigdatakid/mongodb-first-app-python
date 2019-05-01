import pymongo
import pprint
import os

MongoDB_cluster_password = os.environ["MONGODB_CLUSTER_PASSWORD_ENV"]
MongoDB_cluster_name = os.environ["MONGODB_CLUSTER_NAME_ENV"]
MongoDB_user_name = "mongodba"

from pymongo.errors import ConnectionFailure

connectionString = "mongodb+srv://" + MongoDB_user_name + ":" + MongoDB_cluster_password  + "@" + MongoDB_cluster_name
connectionString= connectionString + "/test?retryWrites=true"

# replace <PASSWORD> with user password
client = pymongo.MongoClient()

try:
    status = client.admin.command("serverStatus")
    print("Connected to MongoDB Atlas with status: ")

except ConnectionFailure:
    print("MongoDB Atlas connection not established.")