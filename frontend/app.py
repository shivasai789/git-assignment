from flask import Flask,request,render_template
from datetime import datetime
import requests


app=Flask(__name__) 

BACKEND_URL = "http://127.0.0.1:9000/"


@app.route('/')
def home():
    current_time = datetime.now().strftime('%H:%M:%S')
    
    return render_template('index.html',current_time=current_time)

@app.route('/api')
def second():
    
    name = request.values.get('name') 
    age = request.values.get('age') 
    
    res = {
        'name': name,
        'age': age
    }
    
    return res

@app.route('/add/<name>')
def name(name):
    s = "Hello "+name+"!"
    return s

@app.route('/submit',methods=['POST'])
def submit():
    data = request.form
    
    requests.post(BACKEND_URL + "/submit",json=data)
    
    return "Data submitted successfully!"

@app.route('/get-data')
def getdata():
    response = requests.get(BACKEND_URL + "/view")
    
    return response.json()



if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8000",debug=True) # if we didn't use debug=True then we have restart the file after the changes to reflect