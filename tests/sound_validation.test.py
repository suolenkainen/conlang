#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/conlang

import unittest
from unittest.mock import patch
import sound_validation



class after_sound_validity_check(unittest.TestCase):

    def setUp(self):

        self.s_sound = {"IPA": "s", "classes": ["sibilants", "stridents", "obstruents", "fricatives", "continuants"], "types": ["voiceless", "frontcon", "alveolar"], "rules": []}
        self.u_sound = {'IPA': 'u', "classes": ["vowels"], 'types': ['close', 'back', 'rounded'], 'rules': []}
        self.n_sound = {"IPA": "n", "classes": ["nasals", "occlusives"], "types": ["voiced", "frontcon", "alveloar"], "rules": []}
        self.i_sound = {'IPA': 'i', "classes": ["vowels"], 'types': ['close', 'front', 'unrounded'], 'rules': []}
        self.y_sound = {'IPA': 'y', "classes": ["vowels"], 'types': ['close', 'front', 'rounded'], 'rules': []}

        self.sun_syllable = {'stress': None, 'legal': True, 'syllable': 'sun', 'sounds': [self.s_sound, self.u_sound, self.n_sound]}
        self.ny_syllable = {'stress': None, 'legal': True, 'syllable': 'ny', 'sounds': [self.n_sound, self.y_sound]}
        self.is_syllable = {'stress': None, 'legal': True, 'syllable': 'is', 'sounds': [self.i_sound, self.s_sound]}

        self.sun_word = {"syllables": [self.sun_syllable]}
        self.nyis_word = {"syllables": [self.ny_syllable, self.is_syllable]}


    def test_01_check_type_after_rule_single_syllable_word(self):
        rules = {"after sound": {
                    "types": [["voiced"], ["rounded"], ["unrounded"], ["voiceless"]]}}
        
        indexes = indexes = (0 , 1)
        word = self.sun_word

        result = sound_validation.after_sound_validity_check(rules["after sound"], indexes, word)

        self.assertEqual(result, True)


    def test_02_check_type_after_rule_word_first_sound(self):
        rules = {"after sound": {
                    "IPA": [],
                    "types": [["voiced"], ["rounded"], ["unrounded"], ["voiceless"]], 
                    "classes": []}}
        
        indexes = indexes = (0 , 0)
        result = sound_validation.after_sound_validity_check(rules["after sound"], indexes, self.sun_word,)

        self.assertEqual(result, False)


    def test_03_check_type_after_rule_after_second_syllabe_first_sound(self):
        rules = {"after sound": {
                    "IPA": [],
                    "types": [["voiced"], ["rounded"], ["unrounded"], ["voiceless"]], 
                    "classes": []}}
        
        indexes = indexes = (1 , 0)

        result = sound_validation.after_sound_validity_check(rules["after sound"], indexes, self.sun_word)

        self.assertEqual(result, True)


    def test_04_check_type_after_rule_after_second_syllabe_first_sound_fail(self):
        rules = {"after sound": {
                    "IPA": [],
                    "types": [["trill"]], 
                    "classes": []}}
        
        indexes = indexes = (1 , 0)

        result = sound_validation.after_sound_validity_check(rules["after sound"], indexes, self.sun_word)

        self.assertEqual(result, False)


class between_sounds_Validity_Check(unittest.TestCase):
    
    def setUp(self):
        
        self.s_sound = {"IPA": "s", "classes": ["sibilants", "stridents", "obstruents", "fricatives", "continuants"], "types": ["voiceless", "frontcon", "alveolar"], "rules": []}
        self.u_sound = {'IPA': 'u', "classes": ["vowels"], 'types': ['close', 'back', 'rounded'], 'rules': []}
        self.n_sound = {"IPA": "n", "classes": ["nasals", "occlusives"], "types": ["voiced", "frontcon", "alveloar"], "rules": []}
        self.i_sound = {'IPA': 'i', "classes": ["vowels"], 'types': ['close', 'front', 'unrounded'], 'rules': []}
        self.y_sound = {'IPA': 'y', "classes": ["vowels"], 'types': ['close', 'front', 'rounded'], 'rules': []}

        self.sun_syllable = {'stress': None, 'legal': True, 'syllable': 'sun', 'sounds': [self.s_sound, self.u_sound, self.n_sound]}
        self.ny_syllable = {'stress': None, 'legal': True, 'syllable': 'ny', 'sounds': [self.n_sound, self.y_sound]}
        self.is_syllable = {'stress': None, 'legal': True, 'syllable': 'is', 'sounds': [self.i_sound, self.s_sound]}

        self.sun_word = {"syllables": [self.sun_syllable]}
        self.nysun_word = {"syllables": [self.ny_syllable, self.sun_syllable]}
        self.sunis_word = {"syllables": [self.sun_syllable, self.is_syllable]}
        self.sunsun_word = {"syllables": [self.sun_syllable, self.sun_syllable]}


    def test_01_check_between_sounds_rule_single_syllable_word(self):
        rules = {"between": {
                    "preceeding": {
                        "IPA": [],
                        "types": [["voiceless"]], 
                        "classes": []},
                    "trailing": {
                        "types": [["voiced"]], 
                        "classes": []}}}
        
        indexes = indexes = (0 , 1)
        word = self.sun_word

        result = sound_validation.between_sounds_validity_check(rules["between"], indexes, word)

        self.assertEqual(result, True)


    def test_02_check_between_sounds_rule_zero_indexes(self):
        rules = {"between": {
                        "IPA": [],
                        "types": [["voiceless"]], 
                        "classes": []},
                    "trailing": {
                        "IPA": [],
                        "types": [["voiced"]], 
                        "classes": []}}
        
        indexes = indexes = (0 , 0)
        word = self.sun_word

        result = sound_validation.between_sounds_validity_check(rules["between"], indexes, word)

        self.assertEqual(result, False)


    def test_03_check_between_sounds_rule_higher_syllable_and_sound_counts(self):
        rules = {"between": {
                    "preceeding": {
                        "IPA": [], 
                        "types": [["voiceless"]], 
                        "classes": []}, 
                    "trailing": {
                        "IPA": [], 
                        "types": [["voiced"]], 
                        "classes": []}}}
        
        indexes = indexes = (0 , 2)
        word = self.sun_word

        result = sound_validation.between_sounds_validity_check(rules["between"], indexes, word)

        self.assertEqual(result, False)
    

    def test_04_check_between_sounds_rule_including_next_syllable(self):
        rules = {"between": {
                    "preceeding": {
                        "IPA": [], 
                        "types": [["voiced"]], 
                        "classes": []}, 
                    "trailing": {
                        "IPA": [], 
                        "types": [["voiceless"]], 
                        "classes": []}}}
        
        indexes = indexes = (0 , 2)
        word = self.sunsun_word

        result = sound_validation.between_sounds_validity_check(rules["between"], indexes, word)

        self.assertEqual(result, False)


    def test_05_check_between_sounds_rule_with_one_syllable_mismatch_categories(self):
        rules = {"between": {
                    "preceeding": {
                        "IPA": [], 
                        "types": [["voiceless"]]}, 
                    "trailing": { 
                        "types": [["voiced"]], 
                        "classes": []}}}
        
        indexes = indexes = (0 , 1)
        word = self.sun_word

        result = sound_validation.between_sounds_validity_check(rules["between"], indexes, word)

        self.assertEqual(result, True)


    def test_06_check_between_sounds_rule_with_onset_vowel(self):
        rules = {"between": {
                    "preceeding": {
                        "IPA": [], 
                        "types": [["voiced"]], 
                        "classes": []}, 
                    "trailing": {
                        "IPA": [], 
                        "types": [["voiceless"]], 
                        "classes": []}}}
        
        indexes = indexes = (1 , 0)
        word = self.sunis_word

        result = sound_validation.between_sounds_validity_check(rules["between"], indexes, word)

        self.assertEqual(result, True)


    def test_07_check_between_sounds_rule_with_coda_vowel(self):
        rules = {"between": {
                    "preceeding": {
                        "IPA": [], 
                        "types": [["voiced"]], 
                        "classes": []}, 
                    "trailing": {
                        "IPA": [], 
                        "types": [["voiceless"]], 
                        "classes": []}}}
        
        indexes = indexes = (0 , 1)
        word = self.nysun_word

        result = sound_validation.between_sounds_validity_check(rules["between"], indexes, word)

        self.assertEqual(result, True)


    def test_08_check_type_after_rule_no_match(self):
        rules = {"between": {
                    "preceeding": {
                        "IPA": [], 
                        "types":["trill"], 
                        "classes": []}, 
                    "trailing": {
                        "IPA": [], 
                        "types": [["occlusive"]], 
                        "classes": []}}}
        
        indexes = indexes = (0 , 1)
        word = self.sun_word

        result = sound_validation.between_sounds_validity_check(rules["between"], indexes, word)

        self.assertEqual(result, False)


    def test_09_check_type_after_rule_both_no_and_yes_match(self):
        rules = {"between": {
                    "preceeding": {
                        "IPA": [], 
                        "types":[["trill"], ["voiceless"]], 
                        "classes": []}, 
                    "trailing": {
                        "IPA": [], 
                        "types": [["occlusive"], ["voiced"]], 
                        "classes": []}}}
        
        indexes = indexes = (0 , 1)
        word = self.sun_word

        result = sound_validation.between_sounds_validity_check(rules["between"], indexes, word)

        self.assertEqual(result, True)


    def test_10_check_type_after_rule_both_no_and_yes_match_with_class(self):
        rules = {"between": {
                    "preceeding": {
                        "IPA": [], 
                        "types":[], 
                        "classes": [["fricatives"]]}, 
                    "trailing": {
                        "IPA": [], 
                        "types": [["occlusive"], ["voiced"]], 
                        "classes": []}}}
        
        indexes = indexes = (0 , 1) 
        word = self.sun_word

        result = sound_validation.between_sounds_validity_check(rules["between"], indexes, word)

        self.assertEqual(result, True)


class Sound_Itself_Validity_Check(unittest.TestCase):
    
    def setUp(self):
        
        self.s_sound = {"IPA": "s", "classes": ["sibilants", "stridents", "obstruents", "fricatives", "continuants"], "types": ["voiceless", "frontcon", "alveolar"], "rules": []}
        self.u_sound = {'IPA': 'u', "classes": ["vowels"], 'types': ['close', 'back', 'rounded'], 'rules': []}
        self.n_sound = {"IPA": "n", "classes": ["nasals", "occlusives"], "types": ["voiced", "frontcon", "alveloar"], "rules": []}

        self.sun_syllable = {'stress': None, 'legal': True, 'syllable': 'sun', 'sounds': [self.s_sound, self.u_sound, self.n_sound]}

        self.sun_word = {"syllables": [self.sun_syllable]}


    def test_01_check_matching(self):
        rules = {"sound itself": {"IPA": ["u"],
                               "types": [[]],
                               "classes": []}}
        
        word = self.sun_word
        indexes = (0, 1)

        result = sound_validation.sound_itself_validity_check(rules["sound itself"], indexes, word)

        self.assertEqual(result, True)


    def test_02_check_non_matching(self):
        rules = {"sound itself": {
                    "IPA": ["y"],
                    "classes": [["consonants"]]}}
        
        word = self.sun_word
        indexes = (0, 1)

        result = sound_validation.sound_itself_validity_check(rules["sound itself"], indexes, word)

        self.assertEqual(result, False)


    def test_03_check_matching_from_many(self):
        rules = {"sound itself": {
                    "IPA": ["y", "i", "u"],
                    "types": [[]],
                    "classes": []}}
        
        word = self.sun_word
        indexes = (0, 1)

        result = sound_validation.sound_itself_validity_check(rules["sound itself"], indexes, word)

        self.assertEqual(result, True)


    def test_04_check_matching_from_types(self):
        rules = {"sound itself": {
                    "IPA": [],
                    "types": [["back"]],
                    "classes": []}}
        
        word = self.sun_word
        indexes = (0, 1)

        result = sound_validation.sound_itself_validity_check(rules["sound itself"], indexes, word)

        self.assertEqual(result, True)


    def test_04_check_matching_from_classes(self):
        rules = {"sound itself": {
                    "IPA": [],
                    "types": [],
                    "classes": [["vowels"]]}}
        
        word = self.sun_word
        indexes = (0, 1)

        result = sound_validation.sound_itself_validity_check(rules["sound itself"], indexes, word)

        self.assertEqual(result, True)


    def test_05_check_matching_from_classes(self):
        rules = {"sound itself": {
                    "IPA": [],
                    "types": [],
                    "classes": [["occlusives"], ["vowels"]]}}
        
        word = self.sun_word
        indexes = (0, 1)

        result = sound_validation.sound_itself_validity_check(rules["sound itself"], indexes, word)

        self.assertEqual(result, True)


    def test_06_check_matching_from_cluster_classes(self):
        rules = {"sound itself": {
                    "IPA": [],
                    "types": [],
                    "classes": [["stridents", "obstruents"]]}}
        
        word = self.sun_word
        indexes = (0, 0)

        result = sound_validation.sound_itself_validity_check(rules["sound itself"], indexes, word)

        self.assertEqual(result, True)



class Before_Sounds_Validity_Check(unittest.TestCase):
    
    def setUp(self):
        
        self.s_sound = {"IPA": "s", "classes": ["sibilants", "stridents", "obstruents", "fricatives", "continuants"], "types": ["voiceless", "frontcon", "alveolar"], "rules": []}
        self.u_sound = {'IPA': 'u', "classes": ["vowels"], 'types': ['close', 'back', 'rounded'], 'rules': []}
        self.n_sound = {"IPA": "n", "classes": ["nasals", "occlusives"], "types": ["voiced", "frontcon", "alveloar"], "rules": []}
        self.y_sound = {'IPA': 'y', "classes": ["vowels"], 'types': ['close', 'front', 'rounded'], 'rules': []}

        self.sun_syllable = {'stress': None, 'legal': True, 'syllable': 'sun', 'sounds': [self.s_sound, self.u_sound, self.n_sound]}
        self.ny_syllable = {'stress': None, 'legal': True, 'syllable': 'ny', 'sounds': [self.n_sound, self.y_sound]}

        self.sun_word = {"syllables": [self.sun_syllable]}
        self.nysun_word = {"syllables": [self.ny_syllable, self.sun_syllable]}
        self.ny_word = {"syllables": [self.ny_syllable]}


    def test_01_check_before_sounds_rule_single_syllable_word(self):
        rules = {"before": {
                    "IPA": [],
                    "types": [["voiced"]], 
                    "classes": []}}
        
        indexes = indexes = (0 , 1)
        word = self.sun_word

        result = sound_validation.before_sound_validity_check(rules["before"], indexes, word)

        self.assertEqual(result, True)


    def test_02_check_before_sounds_last_sound_in_word(self):
        rules = {"before": {
                    "IPA": [],
                    "types": [["voiceless"]], 
                    "classes": []}}
        
        indexes = indexes = (0 , 1)
        word = self.ny_word

        result = sound_validation.before_sound_validity_check(rules["before"], indexes, word)

        self.assertEqual(result, False)


    def test_03_check_before_sounds_rule_higher_syllable_and_sound_counts(self):
        rules = {"before": {
                    "IPA": [], 
                    "types": [["voiced"]], 
                    "classes": []}}
        
        indexes = indexes = (0 , 2)
        word = self.sun_word

        result = sound_validation.before_sound_validity_check(rules["before"], indexes, word)

        self.assertEqual(result, False)
    

    def test_04_check_before_sounds_rule_with_one_syllable_mismatch_categories(self):
        rules = {"before": {
                    "types": [["voiced"]]}}
        
        indexes = indexes = (0 , 1)
        word = self.sun_word

        result = sound_validation.before_sound_validity_check(rules["before"], indexes, word)

        self.assertEqual(result, True)


    def test_05_check_before_sounds_rule_with_coda_vowel(self):
        rules = {"before": {
                    "IPA": [], 
                    "types": [["voiceless"]], 
                    "classes": []}}
        
        indexes = indexes = (0 , 1)
        word = self.nysun_word

        result = sound_validation.before_sound_validity_check(rules["before"], indexes, word)

        self.assertEqual(result, True)



# TODO kaikille, missä on nykyään class ja muut, uusi testi (osasta voi poistaa sen, mutta nyt on kaikissa varuilta)


if __name__ == '__main__':
    unittest.main()
