#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/conlang

import unittest
from unittest.mock import patch
import vowel_rounding



class Vowel_Rounding(unittest.TestCase):

    def setUp(self):
        
        self.s_sound = {"IPA": "s", "classes": ["sibilants", "stridents", "obstruents", "fricatives", "continuants"], "types": ["voiceless", "frontcon", "alveolar"], "rules": []}
        self.u_sound = {'IPA': 'u', "classes": ["vowels"], 'types': ['close', 'back', 'rounded'], 'rules': []}
        self.ɯ_sound = {'IPA': 'ɯ', "classes": ["vowels"], 'types': ['close', 'back', 'unrounded'], 'rules': []}
        self.n_sound = {"IPA": "n", "classes": ["nasals", "occlusives"], "types": ["voiced", "frontcon", "alveloar"], "rules": []}
        self.i_sound = {'IPA': 'i', "classes": ["vowels"], 'types': ['close', 'front', 'unrounded'], 'rules': []}
        self.y_sound = {'IPA': 'y', "classes": ["vowels"], 'types': ['close', 'front', 'rounded'], 'rules': []}
        self.ɐ_sound = {'IPA': 'ɐ', "classes": ["vowels"], 'types': ['near-open', 'central'], 'rules': []}
        self.e_sound = {'IPA': 'e', "classes": ["vowels"], 'types': ['close-mid', 'front', 'unrounded'], 'rules': []}
        self.ø_sound = {'IPA': 'ø', "classes": ["vowels"], 'types': ['close-mid', 'front', 'rounded'], 'rules': []}

        self.sun_syllable = {'stress': None, 'legal': True, 'syllable': 'sun', 'sounds': [self.s_sound, self.u_sound, self.n_sound]}
        self.sɯn_syllable = {'stress': None, 'legal': True, 'syllable': 'sɯn', 'sounds': [self.s_sound, self.ɯ_sound, self.n_sound]}
        self.ni_syllable = {'stress': None, 'legal': True, 'syllable': 'ni', 'sounds': [self.n_sound, self.i_sound]}
        self.ny_syllable = {'stress': None, 'legal': True, 'syllable': 'ny', 'sounds': [self.n_sound, self.y_sound]}
        self.sɐs_syllable = {'stress': None, 'legal': True, 'syllable': 'sɐn', 'sounds': [self.s_sound, self.ɐ_sound, self.s_sound]}
        self.is_syllable = {'stress': None, 'legal': True, 'syllable': 'is', 'sounds': [self.i_sound, self.s_sound]}
        self.ys_syllable = {'stress': None, 'legal': True, 'syllable': 'ys', 'sounds': [self.y_sound, self.s_sound]}
        self.sɯs_syllable = {'stress': None, 'legal': True, 'syllable': 'sɯs', 'sounds': [self.s_sound, self.ɯ_sound, self.s_sound]}
        self.sus_syllable = {'stress': None, 'legal': True, 'syllable': 'sus', 'sounds': [self.s_sound, self.u_sound, self.s_sound]}
        self.sɯn_syllable = {'stress': None, 'legal': True, 'syllable': 'sɯn', 'sounds': [self.s_sound, self.ɯ_sound, self.n_sound]}
        self.sun_syllable = {'stress': None, 'legal': True, 'syllable': 'sun', 'sounds': [self.s_sound, self.u_sound, self.n_sound]}
        self.niis_syllable = {'stress': None, 'legal': True, 'syllable': 'niis', 'sounds': [self.n_sound, self.i_sound, self.i_sound, self.s_sound]}
        self.nyis_syllable = {'stress': None, 'legal': True, 'syllable': 'nyis', 'sounds': [self.n_sound, self.y_sound, self.i_sound, self.s_sound]}
        self.nies_syllable = {'stress': None, 'legal': True, 'syllable': 'nies', 'sounds': [self.n_sound, self.i_sound, self.e_sound, self.s_sound]}
        self.nyøs_syllable = {'stress': None, 'legal': True, 'syllable': 'nyøs', 'sounds': [self.n_sound, self.y_sound, self.ø_sound, self.s_sound]}

        self.sunni_word = {"syllables": [self.sun_syllable, self.ni_syllable]}
        self.sunny_word = {"syllables": [self.sun_syllable, self.ny_syllable]}
        self.sɯnni_word = {"syllables": [self.sɯn_syllable, self.ni_syllable]}
        self.nyis_word = {"syllables": [self.ny_syllable, self.is_syllable]}
        self.nyys_word = {"syllables": [self.ny_syllable, self.ys_syllable]}
        self.sɐs_word = {"syllables": [self.sɐs_syllable]}
        self.niissɯs_word = {"syllables": [self.niis_syllable, self.sɯs_syllable]}
        self.nyissus_word = {"syllables": [self.nyis_syllable, self.sus_syllable]}
        self.niessɯs_word = {"syllables": [self.nies_syllable, self.sɯs_syllable]}
        self.nyøssus_word = {"syllables": [self.nyøs_syllable, self.sus_syllable]}
        self.niessɯn_word = {"syllables": [self.nies_syllable, self.sɯn_syllable]}
        self.nyøssun_word = {"syllables": [self.nyøs_syllable, self.sun_syllable]}

        self.sound_list = [self.u_sound, self.y_sound, self.i_sound, self.ɯ_sound, self.s_sound, self.n_sound, self.ɐ_sound, self.e_sound, self.ø_sound]


    @patch('vowel_rounding.between_sounds_validity_check')
    def test_01_rounding_between_any_consonant(self, mock_between_sounds_validity_check):
        
        mock_roundness_rules = {"rounding": {
                                    "between": {}}, 
                                "unrounding": {}}
        
        mock_between_sounds_validity_check.side_effect = [False, True, False, True, True]

        with patch('vowel_rounding.sounds_list', self.sound_list):
            result = vowel_rounding.vowel_roundness(self.sunni_word, mock_roundness_rules)

        self.assertEqual(result, self.sunny_word)


    @patch('vowel_rounding.after_sound_validity_check')
    def test_02_unrounding_with_any_consonant(self, mock_after_sound_validity_check):
        
        mock_roundness_rules = {"unrounding": {
                                    "after sound": {}}, 
                                "rounding": {}}
        
        mock_after_sound_validity_check.side_effect = [False, True, False, True, True]

        with patch('vowel_rounding.sounds_list', self.sound_list):
            result = vowel_rounding.vowel_roundness(self.sunni_word, mock_roundness_rules, True) #FTFTT

        self.assertEqual(result, self.sɯnni_word)


    @patch('vowel_rounding.after_sound_validity_check')
    @patch('vowel_rounding.between_sounds_validity_check')
    def test_03_rounding_with_non_roundable_vowel_after_consonant(self, mock_after_sound_validity_check, mock_between_sounds_validity_check):
        
        mock_roundness_rules = {"rounding": {}, 
                                "unrounding": {
                                    "after sound": {}}}
        
        mock_after_sound_validity_check.side_effect = [False, False, False]
        mock_between_sounds_validity_check.side_effect = [False, False, False]

        with patch('vowel_rounding.sounds_list', self.sound_list):
            result = vowel_rounding.vowel_roundness(self.sɐs_word, mock_roundness_rules, True)

        self.assertEqual(result, self.sɐs_word)


    @patch('vowel_rounding.after_sound_validity_check')
    def test_04_rounding_with_non_roundable_vowel_after_any_vowel(self, mock_after_sound_validity_check):
        
        mock_roundness_rules = {"rounding": {
                                    "after sound": {}}, 
                                "unrounding": {}}
        
        mock_after_sound_validity_check.side_effect = [False, True, True, True]
        
        with patch('vowel_rounding.sounds_list', self.sound_list):
            result = vowel_rounding.vowel_roundness(self.nyis_word, mock_roundness_rules)  #FTTT 

        self.assertEqual(result, self.nyys_word)


    @patch('vowel_rounding.after_sound_validity_check')
    @patch('vowel_rounding.between_sounds_validity_check')
    def test_05_rounding_with_with_placement_rules(self, mock_after_sound_validity_check, mock_between_sounds_validity_check):
        
        mock_roundness_rules = {"rounding": {
                                    "after sound": {
                                        "types": [["nasals"]]}, 
                                    "between": {
                                        "preceeding": {
                                            "types": [["front"]], 
                                            "classes": []
                                            }, 
                                        "trailing": {
                                            "types": [["frontcon"]]}}}, 
                                "unrounding": {}}
        
        mock_after_sound_validity_check.side_effect = [False, True, False, False, False, False, False]
        mock_between_sounds_validity_check.side_effect = [False, False, False, False, False, True, False]
        
        with patch('vowel_rounding.sounds_list', self.sound_list):
            result = vowel_rounding.vowel_roundness(self.niissɯs_word, mock_roundness_rules)  #FTTT 

        self.assertEqual(result, self.nyissus_word)


    @patch('vowel_rounding.between_sounds_validity_check')
    @patch('vowel_rounding.after_sound_validity_check')
    @patch('vowel_rounding.sound_itself_validity_check')
    def test_06_rounding_with_with_multiple_rules(self, mock_sound_itself_validity_check, mock_after_sound_validity_check, mock_between_sounds_validity_check):

        mock_roundness_rules = {"rounding": {
                                    "after sound": {}, 
                                    "between": {
                                        "preceeding": {
                                            "IPA": [],
                                            "types": [["frontcon"]]}, 
                                        "trailing": {
                                            "types": [["frontcon"]], 
                                            "classes": []}}, 
                                    "sound itself": {
                                        "IPA": ["e"]}}, 
                                "unrounding": {}}
        
        mock_sound_itself_validity_check.side_effect = [False, False, True, False, False, False, False]
        mock_after_sound_validity_check.side_effect = [False, True, False, False, False, False, False]
        mock_between_sounds_validity_check.side_effect = [False, False, False, True, False, False, False]
        
        with patch('vowel_rounding.sounds_list', self.sound_list):
            result = vowel_rounding.vowel_roundness(self.niessɯs_word, mock_roundness_rules)

        self.assertEqual(result, self.nyøssus_word)


    @patch('vowel_rounding.between_sounds_validity_check')
    @patch('vowel_rounding.after_sound_validity_check')
    @patch('vowel_rounding.sound_itself_validity_check')
    @patch('vowel_rounding.before_sound_validity_check')
    def test_07_rounding_with_with_multiple_rules_and_classes(self, mock_before_sound_validity_check, mock_sound_itself_validity_check, mock_after_sound_validity_check, mock_between_sounds_validity_check):

        mock_roundness_rules = {"rounding": {
                                    "after sound": {
                                        "IPA": [],
                                        "types": [["nasals"]]}, 
                                    "between": {
                                        "preceeding": {
                                            "types": [["frontcon"]], 
                                            "classes": []}, 
                                        "trailing": {
                                            "types": [["frontcon"]]}}, 
                                    "sound itself": {
                                        "IPA": ["e"],
                                        "classes": []}}, 
                                "unrounding": {}}
        
        mock_before_sound_validity_check.side_effect = [False, False, False, False, False, False, False]
        mock_sound_itself_validity_check.side_effect = [False, False, True, False, False, False, False]
        mock_after_sound_validity_check.side_effect = [False, True, False, False, False, False, False]
        mock_between_sounds_validity_check.side_effect = [False, False, False, True, False, False, False]
        
        with patch('vowel_rounding.sounds_list', self.sound_list):
            result = vowel_rounding.vowel_roundness(self.niessɯs_word, mock_roundness_rules)

        self.assertEqual(result, self.nyøssus_word)


    @patch('vowel_rounding.between_sounds_validity_check')
    @patch('vowel_rounding.after_sound_validity_check')
    @patch('vowel_rounding.sound_itself_validity_check')
    @patch('vowel_rounding.before_sound_validity_check')
    def test_08_rounding_with_with_multiple_rules_and_classes_match(self, mock_before_sound_validity_check, mock_sound_itself_validity_check, mock_after_sound_validity_check, mock_between_sounds_validity_check):

        mock_roundness_rules = {"rounding": {
                                    "after sound": {
                                        "IPA": [],
                                        "types": [["nasals"]]}, 
                                    "between": {
                                        "preceeding": {
                                            "types": [["frontcon"]], 
                                            "classes": []}, 
                                        "trailing": {
                                            "types": [["frontcon"]], 
                                            "classes": []}}, 
                                    "sound itself": {
                                        "types": [['close-mid', 'front']]},
                                    "before": {
                                        "classes": [["nasals"]]}}, 
                                "unrounding": {}}
        
        mock_before_sound_validity_check.side_effect = [False, False, False, True, False, False, False]
        mock_sound_itself_validity_check.side_effect = [False, False, True, False, False, False, False]
        mock_after_sound_validity_check.side_effect = [False, True, False, False, False, False, False]
        mock_between_sounds_validity_check.side_effect = [False, False, False, False, False, False, False]
        
        with patch('vowel_rounding.sounds_list', self.sound_list):
            result = vowel_rounding.vowel_roundness(self.niessɯn_word, mock_roundness_rules)

        self.assertEqual(result, self.nyøssun_word)



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

        result = vowel_rounding.after_sound_validity_check(rules, indexes, word)

        self.assertEqual(result, True)


    def test_02_check_type_after_rule_word_first_sound(self):
        rules = {"after sound": {
                    "IPA": [],
                    "types": [["voiced"], ["rounded"], ["unrounded"], ["voiceless"]], 
                    "classes": []}}
        
        indexes = indexes = (0 , 0)
        result = vowel_rounding.after_sound_validity_check(rules, indexes, self.sun_word,)

        self.assertEqual(result, False)


    def test_03_check_type_after_rule_after_second_syllabe_first_sound(self):
        rules = {"after sound": {
                    "IPA": [],
                    "types": [["voiced"], ["rounded"], ["unrounded"], ["voiceless"]], 
                    "classes": []}}
        
        indexes = indexes = (1 , 0)

        result = vowel_rounding.after_sound_validity_check(rules, indexes, self.sun_word)

        self.assertEqual(result, True)


    def test_04_check_type_after_rule_after_second_syllabe_first_sound_fail(self):
        rules = {"after sound": {
                    "IPA": [],
                    "types": [["trill"]], 
                    "classes": []}}
        
        indexes = indexes = (1 , 0)

        result = vowel_rounding.after_sound_validity_check(rules, indexes, self.sun_word)

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

        result = vowel_rounding.between_sounds_validity_check(rules, indexes, word)

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

        result = vowel_rounding.between_sounds_validity_check(rules, indexes, word)

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

        result = vowel_rounding.between_sounds_validity_check(rules, indexes, word)

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

        result = vowel_rounding.between_sounds_validity_check(rules, indexes, word)

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

        result = vowel_rounding.between_sounds_validity_check(rules, indexes, word)

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

        result = vowel_rounding.between_sounds_validity_check(rules, indexes, word)

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

        result = vowel_rounding.between_sounds_validity_check(rules, indexes, word)

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

        result = vowel_rounding.between_sounds_validity_check(rules, indexes, word)

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

        result = vowel_rounding.between_sounds_validity_check(rules, indexes, word)

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

        result = vowel_rounding.between_sounds_validity_check(rules, indexes, word)

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
        
        sound = self.u_sound

        result = vowel_rounding.sound_itself_validity_check(rules, sound)

        self.assertEqual(result, True)


    def test_02_check_non_matching(self):
        rules = {"sound itself": {
                    "IPA": ["y"],
                    "classes": [["consonants"]]}}
        
        sound = self.u_sound

        result = vowel_rounding.sound_itself_validity_check(rules, sound)

        self.assertEqual(result, False)


    def test_03_check_matching_from_many(self):
        rules = {"sound itself": {
                    "IPA": ["y", "i", "u"],
                    "types": [[]],
                    "classes": []}}
        
        sound = self.u_sound

        result = vowel_rounding.sound_itself_validity_check(rules, sound)

        self.assertEqual(result, True)


    def test_04_check_matching_from_types(self):
        rules = {"sound itself": {
                    "IPA": [],
                    "types": [["back"]],
                    "classes": []}}
        
        sound = self.u_sound

        result = vowel_rounding.sound_itself_validity_check(rules, sound)

        self.assertEqual(result, True)


    def test_04_check_matching_from_classes(self):
        rules = {"sound itself": {
                    "IPA": [],
                    "types": [],
                    "classes": [["vowels"]]}}
        
        sound = self.u_sound

        result = vowel_rounding.sound_itself_validity_check(rules, sound)

        self.assertEqual(result, True)


    def test_05_check_matching_from_classes(self):
        rules = {"sound itself": {
                    "IPA": [],
                    "types": [],
                    "classes": [["occlusives"], ["vowels"]]}}
        
        sound = self.u_sound

        result = vowel_rounding.sound_itself_validity_check(rules, sound)

        self.assertEqual(result, True)


    def test_06_check_matching_from_cluster_classes(self):
        rules = {"sound itself": {
                    "IPA": [],
                    "types": [],
                    "classes": [["stridents", "obstruents"]]}}
        
        sound = self.s_sound

        result = vowel_rounding.sound_itself_validity_check(rules, sound)

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

        result = vowel_rounding.before_sound_validity_check(rules, indexes, word)

        self.assertEqual(result, True)


    def test_02_check_before_sounds_last_sound_in_word(self):
        rules = {"before": {
                    "IPA": [],
                    "types": [["voiceless"]], 
                    "classes": []}}
        
        indexes = indexes = (0 , 1)
        word = self.ny_word

        result = vowel_rounding.before_sound_validity_check(rules, indexes, word)

        self.assertEqual(result, False)


    def test_03_check_before_sounds_rule_higher_syllable_and_sound_counts(self):
        rules = {"before": {
                    "IPA": [], 
                    "types": [["voiced"]], 
                    "classes": []}}
        
        indexes = indexes = (0 , 2)
        word = self.sun_word

        result = vowel_rounding.before_sound_validity_check(rules, indexes, word)

        self.assertEqual(result, False)
    

    def test_04_check_before_sounds_rule_with_one_syllable_mismatch_categories(self):
        rules = {"before": {
                    "types": [["voiced"]]}}
        
        indexes = indexes = (0 , 1)
        word = self.sun_word

        result = vowel_rounding.before_sound_validity_check(rules, indexes, word)

        self.assertEqual(result, True)


    def test_05_check_before_sounds_rule_with_coda_vowel(self):
        rules = {"before": {
                    "IPA": [], 
                    "types": [["voiceless"]], 
                    "classes": []}}
        
        indexes = indexes = (0 , 1)
        word = self.nysun_word

        result = vowel_rounding.before_sound_validity_check(rules, indexes, word)

        self.assertEqual(result, True)



# TODO kaikille, missä on nykyään class ja muut, uusi testi (osasta voi poistaa sen, mutta nyt on kaikissa varuilta)



if __name__ == '__main__':
    unittest.main()
