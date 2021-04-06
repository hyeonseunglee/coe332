#!/usr/bin/env python3
import json
import petname
import random
import sys
import uuid
import datetime
import redis

data = {}
heads = ['snake','bull','lion','raven','bunny']

data['animals'] = []

for x in range(0,20):
	data['animals'].append({'head':random.choice(heads),'body':petname.Name()+'-'+petname.Name(),'arms':random.randrange(2,11,2),'legs':random.randrange(3,13,3),'tail':0,'created_on':datetime.datetime.now().isoformat(),'uid':str(uuid.uuid4())})
	data['animals'][x]['tail'] = data['animals'][x]['arms']+data['animals'][x]['legs']
with open("animals.json",'w') as out:
	json.dump(data,out,indent=2) 
