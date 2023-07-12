import unittest

from translator import english_to_french, french_to_english

class test_english_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertNotEqual(english_to_french('hello'), 'hello')

class test_french_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('bonjour'), 'hello')
        self.assertNotEqual(french_to_english('bonjour'), 'bonjour')



unittest.main()

