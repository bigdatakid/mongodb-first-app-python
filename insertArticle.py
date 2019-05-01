import datetime
import pymongo
import pprint
import os

MongoDB_cluster_password = os.environ["MONGODB_CLUSTER_PASSWORD_ENV"]
MongoDB_cluster_name = os.environ["MONGODB_CLUSTER_NAME_ENV"]
MongoDB_user_name = "mongodba"

from pymongo.errors import ConnectionFailure

connectionString = "mongodb+srv://" + MongoDB_user_name + ":" + MongoDB_cluster_password  + "@" + MongoDB_cluster_name


connectionString= connectionString + "/test?retryWrites=true"
blogDatabase = client.blog
usersCollection = blogDatabase.users
articlesCollection = blogDatabase.articles

author = "mrocha"

article = {
    "title": "This is a great post",
    "post_number" :1 
    "body": "The body of the amazing post would go here.",
    "author": author,
    "tags": ["Rocha", "general", "admin", "Oregon"],
    "posted": datetime.datetime.now()
}

# Let's check to make sure the author exists before inserting

if usersCollection.find_one({"username": author}):
    document = articlesCollection.insert_one(article)
    pprint.pprint(article)
else:
    raise ValueError("Author {} is not a current user".format(author))