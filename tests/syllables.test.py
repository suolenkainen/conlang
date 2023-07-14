#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/conlang

import unittest
from syllables import return_rules
from unittest.mock import patch
import syllables


class Combine_Sounds_to_Syllable(unittest.TestCase):

    def test_call_combine_sounds_to_syllable_function(self):
        result = syllables.combine_sounds_to_syllable()

        self.assertEqual(result, None)
    
    def test_feed_sounds_and_expect_syllable(self):

        list_of_sounds = [
            {'IPA': 'ɒ', "classes": ["vowels"], 'types': ['retracted','rounded','low'], 'rules': []},
            {'IPA': 'm̥', 'classes': ["nasals", "occlusives"], 'types': ['voiceless','frontcon','bilabial'], 'rules': []}
        ]
        
        returning_syllable = syllables.combine_sounds_to_syllable(list_of_sounds)

        self.assertEqual(returning_syllable["sounds"], list_of_sounds)
        self.assertEqual(returning_syllable["syllable"], "ɒm̥")
        self.assertEqual(returning_syllable["stress"], None)

    
    def test_feed_no_sounds(self):
        list_of_sounds = []        
        returning_syllable = syllables.combine_sounds_to_syllable(list_of_sounds)

        self.assertEqual(returning_syllable, None)
    

    def test_wrong_syntax(self):
        list_of_sounds = "string"        
        returning_syllable = syllables.combine_sounds_to_syllable(list_of_sounds)

        self.assertRaises(TypeError)
        self.assertEqual(returning_syllable, None)
        

    def test_wrong_syntax_2(self):
        list_of_sounds = [("string",0)]
        returning_syllable = syllables.combine_sounds_to_syllable(list_of_sounds)

        self.assertRaises(TypeError)
        self.assertEqual(returning_syllable, None)
        


class Redefine_More_Than_One_Syllables(unittest.TestCase):

    def test_call_redefine_function(self):
        returning_syllables = syllables.redefine_more_than_one_syllables()        
        
        self.assertEqual(returning_syllables, None)


    def test_wrong_syntax(self):
        syllables_list = "string" 
        returning_list = syllables.redefine_more_than_one_syllables(syllables_list)

        self.assertRaises(TypeError)
        self.assertEqual(returning_list, None)


    def test_feed_single_syllable_and_get_the_same_back(self):
        syllables_list = []
        syllables_list.append({'stress': None, 'syllable': 'ɒm̥', 'sounds': [{'IPA': 'ɒ', "classes": ["vowels"], 'types': ['retracted','rounded','low'], 'rules': []}, 
                                                       {'IPA': 'm̥', 'classes': ["nasals", "occlusives"], 'types': ['voiceless','frontcon','bilabial'], 'rules': []}]})
        returning_syllables = syllables.redefine_more_than_one_syllables(syllables_list)

        self.assertEqual(returning_syllables, 
                         [{'stress': None, 'syllable': 'ɒm̥', 'sounds': 
                           [{'IPA': 'ɒ', "classes": ["vowels"], 'types': ['retracted','rounded','low'], 'rules': []}, 
                            {'IPA': 'm̥', 'classes': ["nasals", "occlusives"], 'types': ['voiceless','frontcon','bilabial'], 'rules': []}]}])


    def test_two_syllables_that_require_no_modification(self):
        syllables_list = []
        syllables_list.append({'stress': None, 'syllable': 'am', 'sounds': [{'IPA': 'a', "classes": ["vowels"], 'types': ['front','raised','low'], 'rules': []}, 
                                                       {'IPA': 'm', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','bilabial'], 'rules': []}]})
        syllables_list.append({'stress': None, 'syllable': 'ky', 'sounds': [{'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []}, 
                                                       {'IPA': 'y', "classes": ["vowels"], 'types': ['front','raised','unrounded','high'], 'rules': []}]})
        returning_syllables = syllables.redefine_more_than_one_syllables(syllables_list)

        self.assertEqual(returning_syllables, [{'stress': None, 'syllable': 'am', 'sounds': 
                                                [{'IPA': 'a', "classes": ["vowels"], 'types': ['front','raised','low'], 'rules': []},
                                                 {'IPA': 'm', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','bilabial'], 'rules': []}]}, 
                                                 {'stress': None, 'syllable': 'ky', 'sounds': 
                                                  [{'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []}, 
                                                   {'IPA': 'y', "classes": ["vowels"], 'types': ['front','raised','unrounded','high'], 'rules': []}]}])

    @patch('rules.illegal_clusters')  # Mock the return_rules
    def test_two_syllables_with_one_missing_vowel(self, mock_illegal_clusters):
        mock_illegal_clusters.return_value = []

        syllables_list = []
        syllables_list.append({'stress': None, 'syllable': 'am', 'sounds': [{'IPA': 'a', "classes": ["vowels"], 'types': ['front','raised','low'], 'rules': []}, 
                                                       {'IPA': 'm', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','bilabial'], 'rules': []}]})
        syllables_list.append({'stress': None, 'syllable': 'k', 'sounds': [{'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []}]})
        returning_syllables = syllables.redefine_more_than_one_syllables(syllables_list)

        self.assertEqual(returning_syllables, [{'stress': None, 'syllable': 'amk', 'sounds': 
                                                [{'IPA': 'a', "classes": ["vowels"], 'types': ['front','raised','low'], 'rules': []},
                                                 {'IPA': 'm', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','bilabial'], 'rules': []},
                                                 {'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []}
                                                 ]}])
        
    @patch('rules.illegal_clusters')  # Mock the return_rules
    def test_two_syllables_with_one_missing_vowel_in_first(self, mock_illegal_clusters):
        mock_illegal_clusters.return_value = []
        
        syllables_list = []
        syllables_list.append({'stress': None, 'syllable': 'k', 'sounds': [{'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []}]})
        syllables_list.append({'stress': None, 'syllable': 'am', 'sounds': [{'IPA': 'a', "classes": ["vowels"], 'types': ['front','raised','low'], 'rules': []}, 
                                                       {'IPA': 'm', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','bilabial'], 'rules': []}]})
        returning_syllables = syllables.redefine_more_than_one_syllables(syllables_list)

        self.assertEqual(returning_syllables, [{'stress': None, 'syllable': 'kam', 'sounds': 
                                                [{'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []},
                                                 {'IPA': 'a', "classes": ["vowels"], 'types': ['front','raised','low'], 'rules': []},
                                                 {'IPA': 'm', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','bilabial'], 'rules': []}
                                                 ]}])
        
    @patch('rules.illegal_clusters')  # Mock the return_rules
    def test_three_syllables_with_one_missing_vowel_in_first_and_third(self, mock_illegal_clusters):
        mock_illegal_clusters.return_value = []
        
        syllables_list = []
        syllables_list.append({'stress': None, 'syllable': 'k', 'sounds': [{'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []}]})
        syllables_list.append({'stress': None, 'syllable': 'am', 'sounds': [{'IPA': 'a', "classes": ["vowels"], 'types': ['front','raised','low'], 'rules': []}, 
                                                       {'IPA': 'm', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','bilabial'], 'rules': []}]})
        syllables_list.append({'stress': None, 'syllable': 'k', 'sounds': [{'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []}]})
        syllables_list.append({'stress': None, 'syllable': 'am', 'sounds': [{'IPA': 'a', "classes": ["vowels"], 'types': ['front','raised','low'], 'rules': []}, 
                                                       {'IPA': 'm', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','bilabial'], 'rules': []}]})
        returning_syllables = syllables.redefine_more_than_one_syllables(syllables_list)

        # self.assertEqual(returning_syllables, [{'stress': None, 'syllable': 'kam', 'sounds': 
        #                                         [{'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []},
        #                                          {'IPA': 'a', "classes": ["vowels"], 'types': ['front','raised','low'], 'rules': []},
        #                                          {'IPA': 'm', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','bilabial'], 'rules': []}
        #                                          ]},
        #                                        {'stress': None, 'syllable': 'kam', 'sounds': 
        #                                         [{'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []},
        #                                          {'IPA': 'a', "classes": ["vowels"], 'types': ['front','raised','low'], 'rules': []},
        #                                          {'IPA': 'm', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','bilabial'], 'rules': []}
        #                                          ]}])
        
    @patch('rules.illegal_clusters')  # Mock the return_rules
    def test_two_illegal_syllables_with_one_missing_vowel(self, mock_illegal_clusters):
        mock_illegal_clusters.return_value = []
        
        syllables_list = []
        syllables_list.append({'stress': None, 'syllable': 'am', 'sounds': [{'IPA': 'a', "classes": ["vowels"], 'types': ['front','raised','low'], 'rules': []},
                                                                            {'IPA': 'm', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','bilabial'], 'rules': []}]})
        syllables_list.append({'stress': None, 'syllable': 'k', 'sounds': [{'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []}, 
                                                                           {'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []}]})
        returning_syllables = syllables.redefine_more_than_one_syllables(syllables_list)

        self.assertEqual(returning_syllables, [{'stress': None, 'syllable': 'amkk', 'sounds': 
                                                [{'IPA': 'a', "classes": ["vowels"], 'types': ['front','raised','low'], 'rules': []},
                                                 {'IPA': 'm', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','bilabial'], 'rules': []},
                                                 {'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []},
                                                 {'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []}
                                                 ]}])
                                                 

    def test_only_two_illegal_syllables(self):
        syllables_list = []
        syllables_list.append({'stress': None, 'syllable': 'k', 'sounds': [{'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []}]})
        syllables_list.append({'stress': None, 'syllable': 'k', 'sounds': [{'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []}]})
        returning_syllables = syllables.redefine_more_than_one_syllables(syllables_list)

        self.assertEqual(returning_syllables, [{'stress': None, 'syllable': 'k', 'sounds': [{'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []}]},
                                               {'stress': None, 'syllable': 'k', 'sounds': [{'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []}]}])
                                                 

if __name__ == '__main__':
    unittest.main()
