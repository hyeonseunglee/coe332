from flask import Flask
import json
import random
import redis
from flask import request
from flask import jsonify
import datetime
from datetime import datetime

app = Flask(__name__)

rd = redis.StrictRedis(host='redis',port=6379, db =12, charset='utf-8',decode_responses=True)

@app.route('/helloworld',methods=['GET'])
def hello_world():
	return 'Hello, world!\n'

@app.route('/hello/<name>',methods=['GET'])
def hello_name(name):
	return 'Hello, {name}!\n'

@app.route('/animals',methods=['GET'])
def get_animals():
	return json.dumps(get_data())

@app.route('/animals/include_in_body/<ani>',methods=['GET'])
def get_bodyanimal(ani):
	test = get_data()
	jsonList = test['animals']
	output =[x for x in jsonList if ani in x['body']]
	return json.dumps(output)

@app.route('/animals/arms/<num>',methods=['GET'])
def get_arms(num):
	test = get_data()
	jsonList = test['animals']
	output =[x for x in jsonList if x['arms'] == int(num)]
	return json.dumps(output)

@app.route('/animals/random',methods=['GET'])
def get_random():
	return get_data4()

### MIDTERM CONTENTS ###

@app.route('/query_by_dates',methods=['GET'])
def querybydates():
	start = request.args.get("startdate",type=str)
	startdate = datetime.strptime(start,"%Y-%m-%dT%H:%M:%S.%f")
	end = request.args.get("enddate",type=str)
	enddate = datetime.strptime(end,"%Y-%m-%dT%H:%M:%S.%f")
	data = []
	for x in rd.keys("*"):
		animal = json.loads(rd.get(x))
		if (startdate <= datetime.strptime(animal["created_on"],"%Y-%m-%dT%H:%M:%S.%f")) and (datetime.strptime(animal["created_on"],"%Y-%m-%dT%H:%M:%S.%f")<=enddate):
			data.append(animal)
	return json.dumps(data)

@app.route('/search_by_ID',methods=['GET'])
def searchbyid():
	ID = request.args.get("uid",type=str)
	return json.dumps(rd.get(ID))

@app.route('/edit_by_ID',methods=['GET'])
def editbyID():
	ID = request.args.get("uid",type=str)
	newhead = request.args.get("newhead",default=None,type=str)
	newbody = request.args.get("newbody",default=None,type=str)
	newarms = request.args.get("newarms",default=None,type=int)
	newlegs = request.args.get("newlegs",default=None,type=int)
	newtail = request.args.get("newtail",default=None,type=int)
	newanimal = json.loads(rd.get(ID))
	if newhead is not None:
		newanimal['head'] = newhead
	if newbody is not None:
		newanimal['body'] = newbody
	if newarms is not None:
		newanimal['arms'] = newarms
	if newlegs is not None:
		newanimal['legs'] = newlegs
	if newtail is not None:
		newanimal['tail'] = newtail
	rd.set(ID,json.dumps(newanimal))
	return json.dumps(newanimal)

@app.route('/delete_by_dates',methods=['GET'])
def deletebydates():
	start = request.args.get("startdate",type=str)
	startdate = datetime.strptime(start,"%Y-%m-%dT%H:%M:%S.%f")
	end = request.args.get("enddate",type=str)
	enddate = datetime.strptime(end,"%Y-%m-%dT%H:%M:%S.%f")
	data1 = []
	counter = 0
	for x in rd.keys("*"):
		animal = json.loads(rd.get(x))
		if (startdate <= datetime.strptime(animal["created_on"],"%Y-%m-%dT%H:%M:%S.%f")) and (datetime.strptime(animal["created_on"],"%Y-%m-%dT%H:%M:%S.%f")<=enddate):
			data1.append(animal)
			counter = counter + 1
	for x in data1:
		rd.delete(x["uid"])
	return json.dumps(data1)

@app.route('/average_legs',methods=['GET'])
def avglegs():
	total=0
	counter=0
	for x in rd.keys('*'):
		animal = json.loads(rd.get(x))
		total = total + animal["legs"]
		counter = counter + 1
	return str(float(total)/float(counter))

@app.route('/total_count',methods=['GET'])
def totalcount():
	return str(len(list(rd.keys('*'))))

@app.route('/redisanimals',methods=['GET'])
def pull():
	data = get_data()
	animals = data['animals']
	for x in range(0,20):
		rd.set(animals[x]['uid'],json.dumps(animals[x]))
	return json.dumps(animals)
def get_data():
	with open("animals.json","r") as json_file:
		data = json.load(json_file)
	return data

def get_data4():
	with open("animals.json","r") as json_file:
		data = json.load(json_file)
		output = data['animals'][random.randint(0,19)]
	return output		

# the next statement should usually appear at the bottom of a flask app
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
