import unittest
from json_ex import check_char_count
from json_ex import check_char_type
from json_ex import check_first_letter

class TestJsonEx(unittest.TestCase):

	def test_check_char_count(self):
		self.assertEqual(check_char_count('AA'), 'AA count passes')
		self.assertEqual(check_char_count('AAA'), 'AAA count FAILS')
		self.assertRaises(AssertionError, check_char_count, 1)
		self.assertRaises(AssertionError, check_char_count, True)
		self.assertRaises(AssertionError, check_char_count, ['AA', 'BB'])

	def test_check_char_type(self):
		self.assertEqual(check_char_type('AA'), 'AA type passes')
		self.assertEqual(check_char_type('Aa'), 'Aa type FAILS')
		self.assertEqual(check_char_type('aa'), 'aa type FAILS')
		self.assertEqual(check_char_type('A1'), 'A1 type FAILS')
		self.assertEqual(check_char_type('a1'), 'a1 type FAILS')
		self.assertRaises(AttributeError, check_char_type, 1)
		self.assertRaises(AttributeError, check_char_type, True)
		self.assertRaises(AttributeError, check_char_type, ['AA', 'BB'])
	def test_check_first_letter(self):
		self.assertEqual(check_first_letter('Al','Alabama'),'first letters match')
		self.assertEqual(check_first_letter('Al','Blabama'),'first letters do not match')
		self.assertRaises(IndexError, check_first_letter, 'Al', '')
if __name__ == '__main__':
	unittest.main()
