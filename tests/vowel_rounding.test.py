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


    @patch('sound_validation.between_sounds_validity_check')
    def test_01_rounding_between_any_consonant(self, mock_between_sounds_validity_check):
        
        mock_roundness_rules = {"rounding": {
                                    "between": {}}, 
                                "unrounding": {}}
        
        mock_between_sounds_validity_check.side_effect = [False, True, False, True, True]

        with patch('vowel_rounding.sounds_list', self.sound_list):
            result = vowel_rounding.vowel_roundness(self.sunni_word, mock_roundness_rules)

        self.assertEqual(result, self.sunny_word)


    @patch('sound_validation.after_sound_validity_check')
    def test_02_unrounding_with_any_consonant(self, mock_after_sound_validity_check):
        
        mock_roundness_rules = {"unrounding": {
                                    "after sound": {}}, 
                                "rounding": {}}
        
        mock_after_sound_validity_check.side_effect = [False, True, False, True, True]

        with patch('vowel_rounding.sounds_list', self.sound_list):
            result = vowel_rounding.vowel_roundness(self.sunni_word, mock_roundness_rules, True) #FTFTT

        self.assertEqual(result, self.sɯnni_word)


    @patch('sound_validation.after_sound_validity_check')
    @patch('sound_validation.between_sounds_validity_check')
    def test_03_rounding_with_non_roundable_vowel_after_consonant(self, mock_after_sound_validity_check, mock_between_sounds_validity_check):
        
        mock_roundness_rules = {"rounding": {}, 
                                "unrounding": {
                                    "after sound": {}}}
        
        mock_after_sound_validity_check.side_effect = [False, False, False]
        mock_between_sounds_validity_check.side_effect = [False, False, False]

        with patch('vowel_rounding.sounds_list', self.sound_list):
            result = vowel_rounding.vowel_roundness(self.sɐs_word, mock_roundness_rules, True)

        self.assertEqual(result, self.sɐs_word)


    @patch('sound_validation.after_sound_validity_check')
    def test_04_rounding_with_non_roundable_vowel_after_any_vowel(self, mock_after_sound_validity_check):
        
        mock_roundness_rules = {"rounding": {
                                    "after sound": {}}, 
                                "unrounding": {}}
        
        mock_after_sound_validity_check.side_effect = [False, True, True, True]
        
        with patch('vowel_rounding.sounds_list', self.sound_list):
            result = vowel_rounding.vowel_roundness(self.nyis_word, mock_roundness_rules)  #FTTT 

        self.assertEqual(result, self.nyys_word)


    @patch('sound_validation.after_sound_validity_check')
    @patch('sound_validation.between_sounds_validity_check')
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


    @patch('sound_validation.between_sounds_validity_check')
    @patch('sound_validation.after_sound_validity_check')
    @patch('sound_validation.sound_itself_validity_check')
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


    @patch('sound_validation.between_sounds_validity_check')
    @patch('sound_validation.after_sound_validity_check')
    @patch('sound_validation.sound_itself_validity_check')
    @patch('sound_validation.before_sound_validity_check')
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


    @patch('sound_validation.between_sounds_validity_check')
    @patch('sound_validation.after_sound_validity_check')
    @patch('sound_validation.sound_itself_validity_check')
    @patch('sound_validation.before_sound_validity_check')
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



if __name__ == '__main__':
    unittest.main()
