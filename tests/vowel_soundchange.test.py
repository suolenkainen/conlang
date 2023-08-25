#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/conlang

import unittest
from unittest.mock import patch
import vowel_soundchange



class Vowel_Rounding(unittest.TestCase):

    def setUp(self):
        
        self.s_sound = {"IPA": "s", "classes": ["sibilants", "stridents", "obstruents", "fricatives", "continuants"], "types": ["voiceless", "frontcon", "alveolar"], "rules": []}
        self.u_sound = {'IPA': 'u', "classes": ["vowels"], 'types': ['close', 'back', 'rounded'], 'rules': []}
        self.ɯ_sound = {'IPA': 'ɯ', "classes": ["vowels"], 'types': ['close', 'back', 'unrounded'], 'rules': []}
        self.n_sound = {"IPA": "n", "classes": ["nasals", "occlusives"], "types": ["voiced", "frontcon", "alveloar"], "rules": []}
        self.i_sound = {'IPA': 'i', "classes": ["vowels"], 'types': ['close', 'front', 'unrounded'], 'rules': []}
        self.y_sound = {'IPA': 'y', "classes": ["vowels"], 'types': ['close', 'front', 'rounded'], 'rules': []}
        self.ɐ_sound = {'IPA': 'ɐ', "classes": ["vowels"], 'types': ['near-open', 'central'], 'rules': []}

        self.sun_syllable = {'stress': None, 'legal': True, 'syllable': 'sun', 'sounds': [self.s_sound, self.u_sound, self.n_sound]}
        self.sɯn_syllable = {'stress': None, 'legal': True, 'syllable': 'sɯn', 'sounds': [self.s_sound, self.ɯ_sound, self.n_sound]}
        self.ni_syllable = {'stress': None, 'legal': True, 'syllable': 'ni', 'sounds': [self.n_sound, self.i_sound]}
        self.ny_syllable = {'stress': None, 'legal': True, 'syllable': 'ny', 'sounds': [self.n_sound, self.y_sound]}
        self.sɐs_syllable = {'stress': None, 'legal': True, 'syllable': 'sɐn', 'sounds': [self.s_sound, self.ɐ_sound, self.s_sound]}
        self.is_syllable = {'stress': None, 'legal': True, 'syllable': 'is', 'sounds': [self.i_sound, self.s_sound]}
        self.ys_syllable = {'stress': None, 'legal': True, 'syllable': 'ys', 'sounds': [self.y_sound, self.s_sound]}
        self.sɯs_syllable = {'stress': None, 'legal': True, 'syllable': 'sis', 'sounds': [self.s_sound, self.ɯ_sound, self.s_sound]}
        self.niis_syllable = {'stress': None, 'legal': True, 'syllable': 'niis', 'sounds': [self.n_sound, self.i_sound, self.i_sound, self.s_sound]}
        self.sus_syllable = {'stress': None, 'legal': True, 'syllable': 'sus', 'sounds': [self.s_sound, self.u_sound, self.s_sound]}
        self.nyis_syllable = {'stress': None, 'legal': True, 'syllable': 'nyis', 'sounds': [self.n_sound, self.y_sound, self.i_sound, self.s_sound]}

        self.sunni_word = {"syllables": [self.sun_syllable, self.ni_syllable]}
        self.sunny_word = {"syllables": [self.sun_syllable, self.ny_syllable]}
        self.sɯnni_word = {"syllables": [self.sɯn_syllable, self.ni_syllable]}
        self.nyis_word = {"syllables": [self.ny_syllable, self.is_syllable]}
        self.nyys_word = {"syllables": [self.ny_syllable, self.ys_syllable]}
        self.sɐs_word = {"syllables": [self.sɐs_syllable]}
        self.niissɯs_word = {"syllables": [self.niis_syllable, self.sɯs_syllable]}
        self.nyissus_word = {"syllables": [self.nyis_syllable, self.sus_syllable]}

        self.sound_list = [self.u_sound, self.y_sound, self.i_sound, self.ɯ_sound, self.s_sound, self.n_sound, self.ɐ_sound]

    @patch('vowel_soundchange.after_type_check')
    @patch('vowel_soundchange.between_types_check')
    def test_rounding_between_any_consonant(self, mock_after_type_check, mock_between_types_check):
        
        mock_roundness_rules = {"rounding": {"between types": ["voiced", "voiceless"]}, "unrounding": {}}
        mock_between_types_check.side_effect = [False, True, False, True, True]

        with patch('vowel_soundchange.sounds_list', self.sound_list):
            result = vowel_soundchange.vowel_roundness(self.sunni_word, mock_roundness_rules)

        self.assertEqual(result, self.sunny_word)


    @patch('vowel_soundchange.after_type_check')
    @patch('vowel_soundchange.between_types_check')
    def test_unrounding_with_any_consonant(self, mock_after_type_check, mock_between_types_check):
        
        mock_roundness_rules = {"unrounding": {"after types": ["voiced", "voiceless"]}, "rounding": {}}
        mock_after_type_check.side_effect = [False, True, False, True, True]

        with patch('vowel_soundchange.sounds_list', self.sound_list):
            result = vowel_soundchange.vowel_roundness(self.sunni_word, mock_roundness_rules, True) #FTFTT

        self.assertEqual(result, self.sɯnni_word)


    @patch('vowel_soundchange.after_type_check')
    @patch('vowel_soundchange.between_types_check')
    def test_rounding_with_non_roundable_vowel_after_consonant(self, mock_after_type_check, mock_between_types_check):
        
        mock_roundness_rules = {"rounding": {"after types": ["voiced", "voiceless"]}, "unrounding": {"after types": ["voiced"]}}
        mock_after_type_check.side_effect = [False, False, False]
        mock_between_types_check.side_effect = [False, False, False]

        with patch('vowel_soundchange.sounds_list', self.sound_list):
            result = vowel_soundchange.vowel_roundness(self.sɐs_word, mock_roundness_rules, True)

        self.assertEqual(result, self.sɐs_word)


    @patch('vowel_soundchange.after_type_check')
    @patch('vowel_soundchange.between_types_check')
    def test_rounding_with_non_roundable_vowel_after_any_vowel(self, mock_after_type_check, mock_between_types_check):
        
        mock_roundness_rules = {"rounding": {"after types": ["voiced", "rounded", "unrounded", "voiceless"]}, "unrounding": {}}
        mock_after_type_check.side_effect = [False, True, True, True]
        
        with patch('vowel_soundchange.sounds_list', self.sound_list):
            result = vowel_soundchange.vowel_roundness(self.nyis_word, mock_roundness_rules)  #FTTT 

        self.assertEqual(result, self.nyys_word)


    @patch('vowel_soundchange.after_type_check')
    @patch('vowel_soundchange.between_types_check')
    def test_rounding_with_with_multiple_rules(self, mock_after_type_check, mock_between_types_check):
    # def test_rounding_with_with_multiple_rules(self, mock_after_type_check):
        
        mock_roundness_rules = {"rounding": {"after types": ["nasals"], "between types": {"preceeding": ["frontcon"], "trailing": ["frontcon"]}}, "unrounding": {}}
        mock_after_type_check.side_effect = [False, True, False, False, False, False, False]
        mock_between_types_check.side_effect = [False, False, False, False, False, True, False]
        
        with patch('vowel_soundchange.sounds_list', self.sound_list):
            result = vowel_soundchange.vowel_roundness(self.niissɯs_word, mock_roundness_rules)  #FTTT 

        self.assertEqual(result, self.nyissus_word)


class Vowel_Dropping(unittest.TestCase):

    def setUp(self):
        pass


    def test_vowel_drop_check(self):
        
        result = vowel_soundchange.vowel_drop("syllables")

        self.assertEqual(result, None)



class After_Type_Check(unittest.TestCase):

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


    def test_check_type_after_rule_single_syllable_word(self):
        rules = {"after types": ["voiced", "rounded", "unrounded", "voiceless"]}
        indexes = indexes = (0 , 1)
        word = self.sun_word

        result = vowel_soundchange.after_type_check(rules, indexes, word)

        self.assertEqual(result, True)


    def test_check_type_after_rule_word_first_sound(self):
        rules = {"after types": ["voiced", "rounded", "unrounded", "voiceless"]}
        indexes = indexes = (0 , 0)
        result = vowel_soundchange.after_type_check(rules, indexes, self.sun_word,)

        self.assertEqual(result, False)


    def test_check_type_after_rule_after_second_syllabe_first_sound(self):
        rules = {"after types": ["voiced", "rounded", "unrounded", "voiceless"]}
        indexes = indexes = (1 , 0)

        result = vowel_soundchange.after_type_check(rules, indexes, self.sun_word)

        self.assertEqual(result, True)


class Between_Types_Check(unittest.TestCase):
    
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


    def test_check_between_types_rule_single_syllable_word(self):
        rules = {"between types": {"preceeding": ["voiceless"], "trailing": ["voiced"]}}
        indexes = indexes = (0 , 1)
        word = self.sun_word

        result = vowel_soundchange.between_types_check(rules, indexes, word)

        self.assertEqual(result, True)


    def test_check_between_types_rule_zero_indexes(self):
        rules = {"between types": {"preceeding": ["voiceless"], "trailing": ["voiced"]}}
        indexes = indexes = (0 , 0)
        word = self.sun_word

        result = vowel_soundchange.between_types_check(rules, indexes, word)

        self.assertEqual(result, False)


    def test_check_between_types_rule_higher_syllable_and_sound_counts(self):
        rules = {"between types": {"preceeding": ["voiceless"], "trailing": ["voiced"]}}
        indexes = indexes = (0 , 2)
        word = self.sun_word

        result = vowel_soundchange.between_types_check(rules, indexes, word)

        self.assertEqual(result, False)
    

    def test_check_between_types_rule_including_next_syllable(self):
        rules = {"between types": {"preceeding": ["voiced"], "trailing": ["voiceless"]}}
        indexes = indexes = (0 , 2)
        word = self.sunsun_word

        result = vowel_soundchange.between_types_check(rules, indexes, word)

        self.assertEqual(result, False)


    def test_check_between_types_rule_with_one_syllable(self):
        rules = {"between types": {"preceeding": ["voiceless"], "trailing": ["voiced"]}}
        indexes = indexes = (0 , 1)
        word = self.sun_word

        result = vowel_soundchange.between_types_check(rules, indexes, word)

        self.assertEqual(result, True)


    def test_check_between_types_rule_with_onset_vowel(self):
        rules = {"between types": {"preceeding": ["voiced"], "trailing": ["voiceless"]}}
        indexes = indexes = (1 , 0)
        word = self.sunis_word

        result = vowel_soundchange.between_types_check(rules, indexes, word)

        self.assertEqual(result, True)


    def test_check_between_types_rule_with_coda_vowel(self):
        rules = {"between types": {"preceeding": ["voiced"], "trailing": ["voiceless"]}}
        indexes = indexes = (0 , 1)
        word = self.nysun_word

        result = vowel_soundchange.between_types_check(rules, indexes, word)

        self.assertEqual(result, True)


    def test_check_type_after_rule_no_match(self):
        rules = {"between types": {"preceeding": ["trill"], "trailing": ["occlusive"]}}
        indexes = indexes = (0 , 1)
        word = self.sun_word

        result = vowel_soundchange.between_types_check(rules, indexes, word)

        self.assertEqual(result, False)



if __name__ == '__main__':
    unittest.main()
