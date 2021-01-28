import json
import petname
import random

data = {}
heads = ['snake','bull','lion','raven','bunny']

data['animals'] = []

for x in range(0,20):
	data['animals'].append({'head':random.choice(heads),'body':petname.Name()+'-'+petname.Name(),'arms':random.randint(2,10),'legs':random.randint(3,12),'tail':0})
	data['animals'][x]['tail'] = data['animals'][x]['arms']+data['animals'][x]['legs']
with open('animals.json','w') as out:
	json.dump(data,out,indent=2) 
