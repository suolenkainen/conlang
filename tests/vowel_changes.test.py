#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/conlang

import unittest
from unittest.mock import patch
import vowel_changes



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
        
        mock_between_sounds_validity_check.side_effect = [False, True, False, False, False]

        with patch('vowel_changes.sounds_list', self.sound_list):
            result = vowel_changes.vowel_roundness(self.sɯnni_word, mock_roundness_rules)

        self.assertEqual(result, self.sunni_word)


    @patch('sound_validation.after_sound_validity_check')
    def test_02_unrounding_with_any_consonant(self, mock_after_sound_validity_check):
        
        mock_roundness_rules = {"unrounding": {
                                    "after sound": {}}, 
                                "rounding": {}}
        
        mock_after_sound_validity_check.side_effect = [False, True, False, True, True]

        with patch('vowel_changes.sounds_list', self.sound_list):
            result = vowel_changes.vowel_roundness(self.sunni_word, mock_roundness_rules, True) #FTFTT

        self.assertEqual(result, self.sɯnni_word)


    @patch('sound_validation.after_sound_validity_check')
    @patch('sound_validation.between_sounds_validity_check')
    def test_03_rounding_with_non_roundable_vowel_after_consonant(self, mock_after_sound_validity_check, mock_between_sounds_validity_check):
        
        mock_roundness_rules = {"rounding": {}, 
                                "unrounding": {
                                    "after sound": {}}}
        
        mock_after_sound_validity_check.side_effect = [False, False, False]
        mock_between_sounds_validity_check.side_effect = [False, False, False]

        with patch('vowel_changes.sounds_list', self.sound_list):
            result = vowel_changes.vowel_roundness(self.sɐs_word, mock_roundness_rules, True)

        self.assertEqual(result, self.sɐs_word)


    @patch('sound_validation.after_sound_validity_check')
    def test_04_rounding_with_non_roundable_vowel_after_any_vowel(self, mock_after_sound_validity_check):
        
        mock_roundness_rules = {"rounding": {
                                    "after sound": {}}, 
                                "unrounding": {}}
        
        mock_after_sound_validity_check.side_effect = [False, True, True, True]
        
        with patch('vowel_changes.sounds_list', self.sound_list):
            result = vowel_changes.vowel_roundness(self.nyis_word, mock_roundness_rules)  #FTTT 

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
        
        with patch('vowel_changes.sounds_list', self.sound_list):
            result = vowel_changes.vowel_roundness(self.niissɯs_word, mock_roundness_rules)  #FTTT 

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
        
        with patch('vowel_changes.sounds_list', self.sound_list):
            result = vowel_changes.vowel_roundness(self.niessɯs_word, mock_roundness_rules)

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
        
        with patch('vowel_changes.sounds_list', self.sound_list):
            result = vowel_changes.vowel_roundness(self.niessɯs_word, mock_roundness_rules)

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
        
        with patch('vowel_changes.sounds_list', self.sound_list):
            result = vowel_changes.vowel_roundness(self.niessɯn_word, mock_roundness_rules)

        self.assertEqual(result, self.nyøssun_word)


class Vowel_Fronting_Tests(unittest.TestCase):

    def setUp(self):
        
        self.s_sound = {"IPA": "s", "classes": ["sibilants", "stridents", "obstruents", "fricatives", "continuants"], "types": ["voiceless", "frontcon", "alveolar"], "rules": []}
        self.n_sound = {"IPA": "n", "classes": ["nasals", "occlusives"], "types": ["voiced", "frontcon", "alveloar"], "rules": []}
        self.u_sound = {'IPA': 'u', "classes": ["vowels"], 'types': ['close', 'back', 'rounded'], 'rules': []}
        self.ʉ_sound = {'IPA': 'ʉ', "classes": ["vowels"], 'types': ['close', 'central', 'rounded'], 'rules': []}
        self.y_sound = {'IPA': 'y', "classes": ["vowels"], 'types': ['close', 'front', 'rounded'], 'rules': []}
        self.ʏ_sound = {'IPA': 'ʏ', "classes": ["vowels"], 'types': ['near-close', 'near-front', 'rounded'], 'rules': []}
        self.ɐ_sound = {'IPA': 'ɐ', "classes": ["vowels"], 'types': ['near-open', 'central'], 'rules': []}
        self.ɑ_sound = {'IPA': 'ɑ', "classes": ["vowels"], 'types': ['open', 'back', 'unrounded'], 'rules': []}

        self.sun_syllable = {'stress': None, 'legal': True, 'syllable': 'sun', 'sounds': [self.s_sound, self.u_sound, self.n_sound]}
        self.sʉn_syllable = {'stress': None, 'legal': True, 'syllable': 'sʉn', 'sounds': [self.s_sound, self.ʉ_sound, self.n_sound]}
        self.syn_syllable = {'stress': None, 'legal': True, 'syllable': 'syn', 'sounds': [self.s_sound, self.y_sound, self.n_sound]}
        self.sʏn_syllable = {'stress': None, 'legal': True, 'syllable': 'sʏn', 'sounds': [self.s_sound, self.ʏ_sound, self.n_sound]}
        self.sɐn_syllable = {'stress': None, 'legal': True, 'syllable': 'sɐn', 'sounds': [self.s_sound, self.ɐ_sound, self.n_sound]}
        self.sɑn_syllable = {'stress': None, 'legal': True, 'syllable': 'sɑn', 'sounds': [self.s_sound, self.ɑ_sound, self.n_sound]}

        self.sun_word = {"syllables": [self.sun_syllable]}
        self.sʉn_word = {"syllables": [self.sʉn_syllable]}
        self.syn_word = {"syllables": [self.syn_syllable]}
        self.sʏn_word = {"syllables": [self.sʏn_syllable]}
        self.sɐn_word = {"syllables": [self.sɐn_syllable]}
        self.sɑn_word = {"syllables": [self.sɑn_syllable]}

        self.sound_list = [self.u_sound, self.s_sound, self.n_sound, self.ʉ_sound, self.y_sound, self.ʏ_sound, self.ɐ_sound, self.ɑ_sound]

    ### Lisää säännöt typelle, IPAlle ja classeille
    def test_01(self):
        # Fronting a back vowel to center as weak move
        
        mock_fronting_rules = {"fronting": {
                                "sound itself": {
                                    "IPA": ["u"]}}}        

        with patch('vowel_changes.sounds_list', self.sound_list):
            result = vowel_changes.vowel_fronting(mock_fronting_rules, self.sun_word, True, False)

        self.assertEqual(result, self.sʉn_word)


    def test_02(self):
        # Fronting a middle vowel to front as weak (non-weak)
        
        mock_fronting_rules = {"fronting": {
                                "sound itself": {
                                    "IPA": ["u"]}}}

        with patch('vowel_changes.sounds_list', self.sound_list):
            result = vowel_changes.vowel_fronting(mock_fronting_rules, self.sun_word, True, True)

        self.assertEqual(result, self.syn_word)


    def test_03(self):
        # Fronting a center vowel to front as strong move (exception)
        
        mock_fronting_rules = {"fronting": {
                                "sound itself": {
                                    "IPA": ["ʉ"]}}}

        with patch('vowel_changes.sounds_list', self.sound_list):
            result = vowel_changes.vowel_fronting(mock_fronting_rules, self.sʉn_word, True, True)

        self.assertEqual(result, self.syn_word)


    def test_04(self):
        # Rearing back vowel
        
        mock_fronting_rules = {"rearing": {
                                "sound itself": {
                                    "IPA": ["u"]}}}
        

        with patch('vowel_changes.sounds_list', self.sound_list):
            result = vowel_changes.vowel_fronting(mock_fronting_rules, self.sun_word, False, False)

        self.assertEqual(result, self.sun_word)


    def test_05(self):
        # Fronting a near-front vowel to front as weak (exception)
        
        mock_fronting_rules = {"fronting": {
                                "sound itself": {
                                    "IPA": ["ʏ"]}}}
        
        with patch('vowel_changes.sounds_list', self.sound_list):
            result = vowel_changes.vowel_fronting(mock_fronting_rules, self.sʏn_word, True, True)

        self.assertEqual(result, self.syn_word)


    def test_06(self):
        # Rearing ɐ-sound
        
        mock_fronting_rules = {"rearing": {
                                "sound itself": {
                                    "IPA": ["ɐ"]}}}
        
        with patch('vowel_changes.sounds_list', self.sound_list):
            result = vowel_changes.vowel_fronting(mock_fronting_rules, self.sɐn_word, False, True)

        self.assertEqual(result, self.sɑn_word)


    def test_08(self):
        # Rearing non-matching rule
        
        mock_fronting_rules = {"rearing": {
                                "sound itself": {
                                    "IPA": ["q"]}}}
        
        with patch('vowel_changes.sounds_list', self.sound_list):
            result = vowel_changes.vowel_fronting(mock_fronting_rules, self.sɐn_word, False, True)

        self.assertEqual(result, self.sɐn_word)



if __name__ == '__main__':
    unittest.main()
