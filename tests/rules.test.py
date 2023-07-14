#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/conlang

import unittest
from unittest.mock import patch
import rules

class Combine_Sounds_to_Syllable(unittest.TestCase):

    def test_call_illegal_clusters(self):
        mock_rules_list = {"clusters": {"illegal consonant clusters": ["ks","sk"]}}

        with patch('rules.rules_list', mock_rules_list):  # Mock the global variable within the test case
            result_sound, result_syllable = rules.analyze_rules()

            self.assertEqual(result_sound, None)
            self.assertEqual(result_syllable, None)


    def test_call_illegal_clusters_2(self):
        mock_rules_list = {"clusters": {"illegal consonant clusters": ["as","sa"]}}

        with patch('rules.rules_list', mock_rules_list):  # Mock the global variable within the test case
            result_sound, result_syllable = rules.analyze_rules(None, None)

            self.assertEqual(result_sound, None)
            self.assertEqual(result_syllable, None)


    def test_no_rules_set_to_sounds(self):
        mock_rules_list = {"clusters": {"illegal consonant clusters": ["as","sa"]}}
        mock_sounds_list = {"clusters": {"illegal consonant clusters": ["as","sa"]}}

        with patch('rules.rules_list', mock_rules_list):
            with patch('rules.sounds_list', mock_sounds_list):  # Mock the global variable within the test case
                result_sound, result_syllable = rules.analyze_rules(None, None)

            self.assertEqual(result_sound, None)
            self.assertEqual(result_syllable, None)


class Set_Rules_for_Sounds(unittest.TestCase):

    def test_call_set_rules_for_sounds(self):
        mock_rules_list = {"clusters": {"illegal consonant clusters": ["as","sa"]}}
        mock_sounds_list = {"clusters": {"illegal consonant clusters": ["as","sa"]}}

        with patch('rules.rules_list', mock_rules_list) and patch('rules.sounds_list', mock_sounds_list):
                result = rules.set_rules_for_sounds(None, None)

                self.assertEqual(result, None)


    def test_one_sound_one_rule(self):
        mock_rules_list = {"clusters": {"illegal vowel clusters": ["a"]}}
        mock_sounds_list = {"vowels": [{'IPA': 'a', "classes": ["vowels"], 'types': ['front','raised','low'], 'rules': []}]}
 
        with patch('rules.rules_list', mock_rules_list) and patch('rules.sounds_list', mock_sounds_list):
                result = rules.set_rules_for_sounds(mock_rules_list, mock_sounds_list)

                self.assertEqual(result, {"vowels": [{'IPA': 'a', "classes": ["vowels"], 
                                                     'types': ['front','raised','low'], 
                                                     'rules': [{'clusters': {'illegal vowel clusters': ["a"]}}]}]
                                                     })


if __name__ == '__main__':
    unittest.main()
