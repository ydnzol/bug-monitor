#!/usr/bin/python
 
import pymongo
 
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
 
mydb = myclient['bug_monitor']
 
collist = mydb.list_collection_names()
# collist = mydb.collection_names()
if "sites" in collist:
  print("Has!")
