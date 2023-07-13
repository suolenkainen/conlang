#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/conlang

import unittest
import syllables


class Combine_Sounds_to_Syllable(unittest.TestCase):

    def test_call_combine_sounds_to_syllable_function(self):
        result = syllables.combine_sounds_to_syllable()

        self.assertEqual(result, None)
    

    def test_feed_sounds_and_expect_syllable(self):
        list_of_sounds = []
        list_of_sounds.append({'IPA': 'ɒ', "classes": ["vowels"], 'types': ['retracted','rounded','low'], 'forbidden': []})
        list_of_sounds.append({'IPA': 'm̥', 'classes': ["nasals", "occlusives"], 'types': ['voiceless','frontcon','bilabial'], 'forbidden': []})
        
        returning_syllable = syllables.combine_sounds_to_syllable(list_of_sounds)

        self.assertEqual(returning_syllable["sounds"], [{'IPA': 'ɒ', 'classes': ['vowels'], 'types': ['retracted', 'rounded', 'low'], 'forbidden': []}, 
                                             {'IPA': 'm̥', 'classes': ['nasals', 'occlusives'], 'types': ['voiceless', 'frontcon', 'bilabial'], 'forbidden': []}])
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
        syllables_list.append({'stress': None, 'syllable': 'ɒm̥', 'sounds': [{'IPA': 'ɒ', "classes": ["vowels"], 'types': ['retracted','rounded','low'], 'forbidden': []}, 
                                                       {'IPA': 'm̥', 'classes': ["nasals", "occlusives"], 'types': ['voiceless','frontcon','bilabial'], 'forbidden': []}]})
        returning_syllables = syllables.redefine_more_than_one_syllables(syllables_list)

        self.assertEqual(returning_syllables, 
                         [{'stress': None, 'syllable': 'ɒm̥', 'sounds': 
                           [{'IPA': 'ɒ', "classes": ["vowels"], 'types': ['retracted','rounded','low'], 'forbidden': []}, 
                            {'IPA': 'm̥', 'classes': ["nasals", "occlusives"], 'types': ['voiceless','frontcon','bilabial'], 'forbidden': []}]}])

    

if __name__ == '__main__':
    unittest.main()
