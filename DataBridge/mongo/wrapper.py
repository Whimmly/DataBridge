from pymongo import MongoClient
import os


if os.path.exists('/.dockerenv'):
  host = 'mongo'
else:
  host = 'localhost'


client = MongoClient(host, 27017)
