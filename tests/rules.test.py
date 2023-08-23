#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/conlang

import unittest
from unittest.mock import patch
import rules

class Combine_Sounds_to_Syllable(unittest.TestCase):

    def setUp(self):
        self.a_sound = {'IPA': 'a', "classes": ["vowels"], 'types': ['front','raised','low'], 'rules': []}
        self.m_sound = {'IPA': 'm', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','bilabial'], 'rules': []}

        self.am_syllable = {'stress': None, 'legal': True, 'syllable': 'am', 'sounds': [self.a_sound, self.m_sound]}


    def test_mock_example(self):
        
        result_sound, result_syllable = rules.analyze_rules([], [])

        self.assertEqual(result_sound, [])
        self.assertEqual(result_syllable, [])


    @patch('rules.analyze_cluster_rules')  # Mock the return_rules
    def test_one_vowel_without_illegal_rules(self, mock_analyze_cluster_rules):

        mock_transferring_sound = [self.a_sound]
        mock_target_syllable = self.am_syllable

        mock_analyze_cluster_rules.return_value = True

        result_sounds, result_syllable = rules.analyze_rules(mock_transferring_sound, mock_target_syllable)

        self.assertEqual(result_sounds, [self.a_sound])
        self.assertEqual(result_syllable, [])


    @patch('rules.analyze_cluster_rules')  # Mock the return_rules
    def test_one_vowel_with_illegal_rules_not_blocking(self, mock_analyze_cluster_rules):

        self.a_sound['rules'] = [{'clusters': {'illegal consonant clusters': ["m","s"]}}]

        transferring_sound = [self.a_sound]
        target_syllable = self.am_syllable

        mock_analyze_cluster_rules.return_value = True

        result_sounds, result_syllable = rules.analyze_rules(transferring_sound, target_syllable)

        self.assertEqual(result_sounds, [self.a_sound])
        self.assertEqual(result_syllable, [])


    @patch('rules.analyze_cluster_rules')  # Mock the return_rules
    def test_one_vowel_with_illegal_rules_blocking(self, mock_analyze_cluster_rules):
        # syllable "am" + "a" -> "ama", but "ma" is blocked thus "a" remains
        self.a_sound['rules'] = [{'clusters': {'illegal clusters': ["m","a"]}}]

        transferring_sound = [self.a_sound]
        target_syllable = self.am_syllable

        mock_analyze_cluster_rules.return_value = False

        result_sounds, result_syllable = rules.analyze_rules(transferring_sound, target_syllable)

        self.assertEqual(result_sounds, [])
        self.assertEqual(result_syllable, [self.a_sound])


    @patch('rules.analyze_cluster_rules')  # Mock the return_rules
    def test_one_vowel_with_illegal_rules_blocking_non_appending(self, mock_analyze_cluster_rules):
        # syllable "a" + "am" + "a" -> "aam", but "aa" is blocked
        self.a_sound['rules'] = [{'clusters': {'illegal clusters': ["aa"]}}, {'clusters': {'illegal clusters': ["a","a"]}}]

        mock_transferring_sound = [self.a_sound]
        mock_target_syllable = self.am_syllable

        mock_analyze_cluster_rules.return_value = False

        result_sounds, result_syllable = rules.analyze_rules(mock_transferring_sound, mock_target_syllable, False)

        self.assertEqual(result_sounds, [])
        self.assertEqual(result_syllable, [self.a_sound])



class Set_Rules_for_Sounds(unittest.TestCase):

    def test_one_sound_one_rule(self):
        mock_rules_list = {"clusters": {"illegal vowel clusters": ["a"]}}
        mock_sounds_list = {"vowels": [{'IPA': 'a', "classes": ["vowels"], 'types': ['front','raised','low'], 'rules': []}]}
 
        with patch('rules.rules_list', mock_rules_list) and patch('rules.sounds_list', mock_sounds_list):
                result = rules.set_rules_for_sounds(mock_rules_list, mock_sounds_list)

                self.assertEqual(result, {"vowels": [{'IPA': 'a', "classes": ["vowels"], 
                                                     'types': ['front','raised','low'], 
                                                     'rules': [{'clusters': {'illegal vowel clusters': ["a"]}}]}]
                                                     })



class Analyze_Cluster_Rules(unittest.TestCase):

    def setUp(self):
        self.a_sound = {'IPA': 'a', "classes": ["vowels"], 'types': ['front','raised','low'], 'rules': []}
        self.m_sound = {'IPA': 'm', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','bilabial'], 'rules': []}


    def test_analyze_cluster_rules_empty(self):
        result = rules.analyze_cluster_rules([], [], {})

        self.assertEqual(result, None)


    def test_analyze_cluster_rules_no_violation(self):

        mock_rule = {'clusters': {'illegal clusters': ["a", "s"]}}
        result = rules.analyze_cluster_rules(self.a_sound, self.m_sound, mock_rule)

        self.assertEqual(result, True)


    def test_analyze_cluster_rules_violation(self):

        mock_rule = {'clusters': {'illegal clusters': [["a", "m"]]}}
        result = rules.analyze_cluster_rules(self.a_sound, self.m_sound, mock_rule)

        self.assertEqual(result, False)



if __name__ == '__main__':
    unittest.main()
