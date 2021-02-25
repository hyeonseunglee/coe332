import unittest
from read_animals import stats

GOOD_INPUT = {'animals': [{'head': 'bull', 'body': 'skunk-mayfly', 'arms': 2, 'legs': 3, 'tail': 5},{'head': 'bull', 'body': 'skunk-mayfly', 'arms': 2, 'legs': 3, 'tail': 5}]}
BAD_INPUT = {'animals': [{'head': 'bull', 'body': 'skunk-mayfly', 'arms': 'two', 'legs': 3, 'tail': 9},{'head': 'bull', 'body': 'skunk-mayfly', 'arms': 2, 'legs': 3, 'tail': 5}]}
class TestReadAnimals(unittest.TestCase):
	
	def test_stats(self):
		self.assertEqual(stats(GOOD_INPUT),{'meanArms':2.0,'meanLegs':3.0,'meanTails':5.0,'modeArms':[2],'modeLegs':[3],'modeTails':[5]})
		self.assertEqual(stats(BAD_INPUT),"Json values are in incorrect type(s).")
		self.assertRaises(TypeError, stats, 1)
		self.assertRaises(KeyError, stats, {'head': 'bull', 'body': 'skunk-mayfly', 'arms': 6, 'legs': 3, 'tail': 9})
		self.assertRaises(KeyError, stats, {'animals':[{'head': 'bull', 'body': 'skunk-mayfly'}]})

if __name__ == '__main__':
	unittest.main()
