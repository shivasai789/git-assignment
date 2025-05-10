from flask import Flask,request,render_template
from datetime import datetime
from dotenv import load_dotenv 
import os 
from pymongo.mongo_client import MongoClient

load_dotenv()

# Create a new client and connect to the server
client = MongoClient(os.getenv('MONGO_URL'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
db = client.test 

collection = db['flask']   

app=Flask(__name__) 

@app.route('/submit', methods=['POST'])
def submit():
    res = request.get_json()
    
    collection.insert_one(res)
    
    return "Data submitted successfully!"

@app.route('/view')
def view():
    data = collection.find()
    
    data = list(data)
    
    for item in data:
        del item['_id']
    
    res = {
        "data": data
    }
    
    return res

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="9000",debug=True) # if we didn't use debug=True then we have restart the file after the changes to reflect