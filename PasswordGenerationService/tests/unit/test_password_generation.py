import json

from password_generation.util.generators import random_word, random_symbol
from password_generation.handlers import generate_password
from unittest import TestCase


class TestPasswordGeneration(TestCase):
    def test_random_word(self):
        word_1 = random_word(1, seed=1)
        word_2 = random_word(1, seed=2)
        self.assertGreater(len(word_1), 0)
        self.assertGreater(len(word_2), 0)
        self.assertNotEqual(word_1, word_2)

    def test_random_symbol(self):
        symbol_1 = random_symbol(1, seed=1)
        symbol_2 = random_symbol(1, seed=2)
        self.assertEqual(len(symbol_1), 1)
        self.assertEqual(len(symbol_2), 1)

    def test_get_password(self):
        expected_result = {
            'statusCode': 200,
            'body': {
                'password': r'[A-Z]{1}.*[0-9]{2}.*$'
            }
        }
        result = json.loads(generate_password({}, None))
        self.assertEqual(result['statusCode'], 200)
        self.assertRegexpMatches(result['body']['password'], expected_result['body']['password'])
