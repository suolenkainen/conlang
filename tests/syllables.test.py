#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/conlang

import unittest
from syllables import return_rules
from unittest.mock import patch
import syllables


class Combine_Sounds_to_Syllable(unittest.TestCase):
    

    def setUp(self):
        self.a_sound = {'IPA': 'a', "classes": ["vowels"], 'types': ['front','raised','low'], 'rules': []}
        self.m_sound = {'IPA': 'm', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','bilabial'], 'rules': []}
        self.s_sound = {'IPA': 's', 'classes': ["sibilants", "stridents", "obstruents", "fricatives", "continuants"], 'types': ['voiceless','frontcon','alveolar'], 'rules': []}


    def test_feed_2_sounds_and_expect_legal_syllable(self):

        list_of_sounds = [self.a_sound, self.m_sound]
        
        returning_syllable = syllables.combine_sounds_to_syllable(list_of_sounds)

        self.assertEqual(returning_syllable["sounds"], list_of_sounds)
        self.assertEqual(returning_syllable["syllable"], "am")
        self.assertEqual(returning_syllable["stress"], None)
        self.assertEqual(returning_syllable["legal"], True)


    def test_feed_2_sounds_and_expect_illegal_syllable(self):

        list_of_sounds = [self.m_sound, self.s_sound]
        
        returning_syllable = syllables.combine_sounds_to_syllable(list_of_sounds)

        self.assertEqual(returning_syllable["sounds"], list_of_sounds)
        self.assertEqual(returning_syllable["syllable"], "ms")
        self.assertEqual(returning_syllable["stress"], None)
        self.assertEqual(returning_syllable["legal"], False)
        

    def test_feed_3_sounds_and_expect_legal_syllable(self):

        list_of_sounds = [self.a_sound, self.m_sound, self.s_sound]
        
        returning_syllable = syllables.combine_sounds_to_syllable(list_of_sounds)

        self.assertEqual(returning_syllable["sounds"], list_of_sounds)
        self.assertEqual(returning_syllable["syllable"], "ams")
        self.assertEqual(returning_syllable["stress"], None)
        self.assertEqual(returning_syllable["legal"], True)

    
    def test_feed_no_sounds(self):
        list_of_sounds = []        
        returning_syllable = syllables.combine_sounds_to_syllable(list_of_sounds)

        self.assertEqual(returning_syllable, None)
    

    def test_wrong_syntax_2(self):
        list_of_sounds = [("string",0)]
        returning_syllable = syllables.combine_sounds_to_syllable(list_of_sounds)

        self.assertRaises(TypeError)
        self.assertEqual(returning_syllable, None)
        


class Redefine_More_Than_One_Syllables(unittest.TestCase):

    def setUp(self):
        self.a_sound = {'IPA': 'a', "classes": ["vowels"], 'types': ['front','raised','low'], 'rules': []}
        self.m_sound = {'IPA': 'm', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','bilabial'], 'rules': []}
        self.s_sound = {'IPA': 's', 'classes': ["sibilants", "stridents", "obstruents", "fricatives", "continuants"], 'types': ['voiceless','frontcon','alveolar'], 'rules': []}
        self.k_sound = {'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []}
        self.y_sound = {'IPA': 'y', "classes": ["vowels"], 'types': ['front','raised','unrounded','high'], 'rules': []}


    def test_wrong_syntax(self):
        syllables_list = "string" 
        returning_list = syllables.redefine_more_than_one_syllables(syllables_list)

        self.assertRaises(TypeError)
        self.assertEqual(returning_list, None)



    def test_two_syllables_that_require_no_modification(self):
        syllables_list = []
        syllables_list.append({'stress': None, 'legal': True, 'syllable': 'am', 'sounds': [self.a_sound, self.m_sound]})
        syllables_list.append({'stress': None, 'legal': True, 'syllable': 'ky', 'sounds': [self.k_sound, self.y_sound]})
        returning_syllables = syllables.redefine_more_than_one_syllables(syllables_list)

        self.assertEqual(returning_syllables, [{'stress': None, 'legal': True, 'syllable': 'am', 'sounds': [self.a_sound, self.m_sound]}, 
                                                 {'stress': None, 'legal': True, 'syllable': 'ky', 'sounds': [self.k_sound, self.y_sound]}])


    @patch('rules.analyze_rules')  # Mock the return_rules
    def test_two_syllables_with_one_missing_vowel(self, mock_analyze_rules):
        mock_analyze_rules.return_value = ["test_two_syllables_with_one_missing_vowel"],[1]

        syllables_list = []
        syllables_list.append({'stress': None, 'legal': True, 'syllable': 'am', 'sounds': [self.a_sound, self.m_sound]})
        syllables_list.append({'stress': None, 'legal': False, 'syllable': 'k', 'sounds': [self.k_sound]})

        mock_analyze_rules.return_value = [self.k_sound],[]
        
        returning_syllables = syllables.redefine_more_than_one_syllables(syllables_list)

        self.assertEqual(returning_syllables, [{'stress': None, 'legal': True, 'syllable': 'amk', 'sounds': 
                                                [self.a_sound, self.m_sound, self.k_sound]}])
        

    @patch('rules.analyze_rules')  # Mock the return_rules
    def test_two_syllables_with_one_missing_vowel_in_first(self, mock_analyze_rules):
        
        syllables_list = []
        syllables_list.append({'stress': None, 'legal': False, 'syllable': 'k', 'sounds': [self.k_sound]})
        syllables_list.append({'stress': None, 'legal': True, 'syllable': 'am', 'sounds': [self.a_sound, self.m_sound]})
        
        mock_add_sounds = [self.k_sound]
        mock_illegal_sounds = []
        mock_analyze_rules.return_value = mock_add_sounds, mock_illegal_sounds
        
        returning_syllables = syllables.redefine_more_than_one_syllables(syllables_list)

        self.assertEqual(returning_syllables, [{'stress': None, 'legal': True, 'syllable': 'kam', 'sounds': 
                                                [self.k_sound,self.a_sound, self.m_sound]}])
        

    @patch('rules.analyze_rules')  # Mock the return_rules
    def test_four_syllables_with_one_missing_vowel_in_first_and_third(self, mock_analyze_rules):

        syllables_list = []
        syllables_list.append({'stress': None, 'legal': False, 'syllable': 'k', 'sounds': [self.k_sound]})
        syllables_list.append({'stress': None, 'legal': True, 'syllable': 'am', 'sounds': [self.a_sound, self.m_sound]})
        syllables_list.append({'stress': None, 'legal': False, 'syllable': 'k', 'sounds': [self.k_sound]})
        syllables_list.append({'stress': None, 'legal': True, 'syllable': 'am', 'sounds': [self.a_sound, self.m_sound]})  

        mock1_add_sounds = [self.k_sound]
        mock1_illegal_sounds = []
        mock2_add_sounds = [self.k_sound]
        mock2_illegal_sounds = []

        mock_analyze_rules.side_effect = [(mock1_add_sounds, mock1_illegal_sounds),(mock2_add_sounds, mock2_illegal_sounds)]
        
        returning_syllables = syllables.redefine_more_than_one_syllables(syllables_list)

        self.assertEqual(returning_syllables, [{'stress': None, 'legal': True, 'syllable': 'kamk', 'sounds': 
                                                [self.k_sound,self.a_sound, self.m_sound, self.k_sound]},
                                               {'stress': None, 'legal': True, 'syllable': 'am', 'sounds': 
                                                [self.a_sound, self.m_sound]}])
        
        
    @patch('rules.analyze_rules')  # Mock the return_rules
    def test_two_syllables_with_one_missing_vowel(self, mock_analyze_rules):
        
        syllables_list = []
        syllables_list.append({'stress': None, 'legal': True, 'syllable': 'am', 'sounds': [self.a_sound, self.m_sound]})
        syllables_list.append({'stress': None, 'legal': False, 'syllable': 'kk', 'sounds': [self.k_sound, self.k_sound]})
        
        mock_add_sounds = [self.k_sound, self.k_sound]
        mock_illegal_sounds = []
        mock_analyze_rules.return_value = mock_add_sounds, mock_illegal_sounds
                
        returning_syllables = syllables.redefine_more_than_one_syllables(syllables_list)

        self.assertEqual(returning_syllables, [{'stress': None, 'legal': True, 'syllable': 'amkk', 'sounds': 
                                                [self.a_sound, self.m_sound, self.k_sound, self.k_sound]}])
                                                 

    def test_only_two_illegal_syllables(self):
        syllables_list = []
        syllables_list.append({'stress': None, 'legal': False, 'syllable': 'k', 'sounds': [self.k_sound]})
        syllables_list.append({'stress': None, 'legal': False, 'syllable': 'k', 'sounds': [self.k_sound]})
        returning_syllables = syllables.redefine_more_than_one_syllables(syllables_list)

        self.assertEqual(returning_syllables, None)
                                                 
                                                
    # testi, missä mockataan "säännön rikkominen" 1
    @patch('rules.analyze_rules')  # Mock the return_rules
    def test_two_syllables_with_rule_violation_for_KK_cluster_after(self, mock_analyze_rules):

        syllables_list = []
        syllables_list.append({'stress': None, 'legal': True, 'syllable': 'am', 'sounds': [self.a_sound, self.m_sound]})
        syllables_list.append({'stress': None, 'legal': False, 'syllable': 'kk', 'sounds': [self.k_sound, self.k_sound]})

        mock_add_sounds = [self.k_sound]
        mock_illegal_sounds = [self.k_sound]
        mock_analyze_rules.return_value = mock_add_sounds, mock_illegal_sounds
                
        returning_syllables = syllables.redefine_more_than_one_syllables(syllables_list)

        self.assertEqual(returning_syllables, [{'stress': None, 'legal': True, 'syllable': 'amk', 'sounds': 
                                                [self.a_sound, self.m_sound, self.k_sound]}])


    @patch('rules.analyze_rules')  # Mock the return_rules
    def test_two_syllables_with_rule_violation_for_KK_cluster_before(self, mock_analyze_rules):
        syllables_list = []
        syllables_list.append({'stress': None, 'legal': False, 'syllable': 'mk', 'sounds': [self.m_sound, self.k_sound]})
        syllables_list.append({'stress': None, 'legal': True, 'syllable': 'am', 'sounds': [self.a_sound, self.m_sound]})

        mock_add_sounds = [self.k_sound]
        mock_illegal_sounds = [self.m_sound]
        mock_analyze_rules.return_value = mock_add_sounds, mock_illegal_sounds
                
        returning_syllables = syllables.redefine_more_than_one_syllables(syllables_list)

        self.assertEqual(returning_syllables, [{'stress': None, 'legal': True, 'syllable': 'kam', 'sounds': 
                                                [self.k_sound, self.a_sound, self.m_sound]}])


    @patch('rules.analyze_rules')  # Mock the return_rules
    def test_three_syllables_with_rule_violation_for_KK_cluster_middle(self, mock_analyze_rules):

        syllables_list = []
        syllables_list.append({'stress': None, 'legal': True, 'syllable': 'am', 'sounds': [self.a_sound, self.m_sound]})
        syllables_list.append({'stress': None, 'legal': False, 'syllable': 'kk', 'sounds': [self.k_sound, self.k_sound]})
        syllables_list.append({'stress': None, 'legal': True, 'syllable': 'am', 'sounds': [self.a_sound, self.m_sound]})
        
        mock_add_sounds = [self.k_sound]
        mock_illegal_sounds = [self.k_sound]
        mock_analyze_rules.return_value = mock_add_sounds, mock_illegal_sounds
        
        returning_syllables = syllables.redefine_more_than_one_syllables(syllables_list)

        self.assertEqual(returning_syllables, [{'stress': None, 'legal': True, 'syllable': 'amk', 'sounds': 
                                                [self.a_sound, self.m_sound,self.k_sound]},
                                               {'stress': None, 'legal': True, 'syllable': 'kam', 'sounds': 
                                                [self.k_sound,self.a_sound, self.m_sound
                                                 ]}])


if __name__ == '__main__':
    unittest.main()
