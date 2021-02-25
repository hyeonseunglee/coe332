#!/usr/bin/env python3

import json
import random
from collections import Counter
import sys

def mode(samp):
	c = Counter(samp)
	return [k for k, v in c.items() if v == c.most_common(1)[0][1]]

def stats(animals):
	totalArms = 0.0
	totalLegs = 0.0
	totalTails = 0.0
	armsList = []
	legsList = []
	tailList = []
	count = 0.0
	statsDict = {'meanArms':0.0, 'modeArms':[], 'meanLegs':0.0, 'modeLegs':[], 'meanTails':0.0, 'modeTails':[]}
	isProperJson = True
	for i in animals['animals']:
		count = count + 1.0
		if type(i["arms"]) is int and type(i["legs"]) is int and type(i["tail"]) is int:
			totalArms = totalArms + i["arms"]
			totalLegs = totalLegs + i["legs"]
			totalTails = totalTails + i["tail"]
			armsList.append(i["arms"])
			legsList.append(i["legs"])
			tailList.append(i["tail"])
		else:
			isProperJson = False
			break
	if isProperJson == True:
		statsDict['meanArms'] = totalArms/count
		statsDict['meanLegs'] = totalLegs/count
		statsDict['meanTails'] = totalTails/count
		statsDict['modeArms'] = mode(armsList)
		statsDict['modeLegs'] = mode(legsList)
		statsDict['modeTails'] = mode(tailList)
	
		return statsDict
	else:
		return "Json values are in incorrect type(s)."
def main():
	with open(sys.argv[1],'r') as f:
		animals = json.load(f)
	print("Below is a random animal from the strange island of Dr. Moreau")
	print(animals['animals'][random.randint(0,19)])
	allStats = stats(animals)
	if type(allStats) is dict:
		print("______________________________________________________________")
		print("--------------Arms, Legs, and Tails Statistics----------------")
		print("______________________________________________________________")
		print("Average Number of Arms")
		print(allStats['meanArms'])
		print("Mode number of Arms")
		for i in allStats['modeArms']:
			print(i)
		print("Average Number of Legs")
		print(allStats['meanLegs'])
		print("Mode Number of Legs")
		for i in allStats['modeLegs']:
			print(i)
		print("Average Number of Tails")
		print(allStats['meanTails'])
		print("Mode Number of Tails")
		for i in allStats['modeTails']:
			print(i)
		
	else:
		print("animals.json has incorret data types as its values.")
if __name__ == '__main__':
	main()

