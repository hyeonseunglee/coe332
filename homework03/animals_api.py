from flask import Flask
import json
import random

app = Flask(__name__)

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
