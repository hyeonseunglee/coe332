from flask import Flask
import json
import random
import flask

app = Flask(__name__)

@app.route('/helloworld',methods=['GET'])
def hello_world():
	return 'Hello, world!\n'

@app.route('/hello/<name>',methods=['GET'])
def hello_name(name):
	return 'Hello, {name}!\n'

@app.route('/animals',methods=['GET'])
def get_animals():
	return get_data()

@app.route('/animals/head/<ani>',methods=['GET'])
def get_heads(ani):
	test = get_data()
	jsonList = test['animals']
	output =[x for x in jsonList if x['head'] == ani]
	return flask.jsonify(output)

@app.route('/animals/legs/<num>',methods=['GET'])
def get_legs(num):
	test = get_data()
	jsonList = test['animals']
	output =[x for x in jsonList if x['legs'] == int(num)]
	return flask.jsonify(output)

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
