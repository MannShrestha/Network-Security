
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# uri = "mongodb+srv://mannshrestha001_db_user:<@password>@cluster0.nowsnmv.mongodb.net/?appName=Cluster0" # later update only password

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)



from pymongo import MongoClient
uri = "mongodb+srv://mannshrestha001_db_user:Admin123@cluster0.nowsnmv.mongodb.net/?appName=Cluster0"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)