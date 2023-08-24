#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/conlang

import unittest
from unittest.mock import patch
import soundchange



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
        self.sunni_word = {"syllables": [self.sun_syllable, self.ni_syllable]}
        self.sunny_word = {"syllables": [self.sun_syllable, self.ny_syllable]}
        self.sɯnni_word = {"syllables": [self.sɯn_syllable, self.ni_syllable]}
        self.sɐs_word = {"syllables": [self.sɐs_syllable]}
        self.sound_list = [self.u_sound, self.y_sound, self.i_sound, self.ɯ_sound, self.s_sound, self.n_sound]


    def test_rounding_with_any_consonant(self):
        
        # mock_roundness_rules = [{"rounding": {"after types": ["voiced"]}}]
        mock_roundness_rules = [{"rounding": {"after types": ["voiced"]}}]

        with patch('soundchange.sounds_list', self.sound_list):
            result = soundchange.vowel_roundness(self.sunni_word, mock_roundness_rules)

        self.assertEqual(result, self.sunny_word)


    def test_unrounding_with_any_consonant(self):
        
        # mock_roundness_rules = [{"rounding": {"after types": ["voiced"]}}]
        mock_roundness_rules = [{"unrounding": {"after types": ["voiced"]}}]

        with patch('soundchange.sounds_list', self.sound_list):
            result = soundchange.vowel_roundness(self.sunni_word, mock_roundness_rules, True)

        self.assertEqual(result, self.sɯnni_word)


    def test_rounding_with_non_roundable_vowel(self):
        
        # mock_roundness_rules = [{"rounding": {"after types": ["voiced"]}}]
        mock_roundness_rules = [{"rounding": {"after types": ["voiced"]}}, {"unrounding": {"after types": ["voiced"]}}]

        with patch('soundchange.sounds_list', self.sound_list):
            result = soundchange.vowel_roundness(self.sɐs_word, mock_roundness_rules, True)

        self.assertEqual(result, self.sɐs_word)


class Vowel_Dropping(unittest.TestCase):

    def setUp(self):
        pass


    def test_vowel_drop_check(self):
        
        result = soundchange.vowel_drop("syllables")

        self.assertEqual(result, None)



if __name__ == '__main__':
    unittest.main()
