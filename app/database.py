
import pymongo

# from .model import UserLoginSchema
from decouple import config


Username = config("username")
Password = config("password")

client = pymongo.MongoClient('mongodb+srv://%s:%s@cluster0.bpkh6lf.mongodb.net/?retryWrites=true&w=majority'% (Username, Password ))

database = client.recommenddb

device_collection = database["device_collection"]

user_collection = database["user_collection"]