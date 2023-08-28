#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/conlang

import json
import sound_validation

file_path = 'rules.json'
with open(file_path, 'r') as file:
    rules_list = json.load(file)
    

file_path = 'sounds.json'
with open(file_path, 'r') as file:
    sounds_list = json.load(file)

roundness_rules = rules_list["vowels"]["roundedness changes"]

fronting_variables = [
    'front', 
    'central', 
    'back']

# Map for exceptions of vowel shifting
fronting_exceptions = {
                        'ɪ': [
                            {'IPA': 'i', "classes": ["vowels"], 'types': ['close', 'front', 'unrounded'], 'rules': []}, 
                            {'IPA': 'ɨ', "classes": ["vowels"], 'types': ['close', 'central', 'unrounded'], 'rules': []}], 
                        'ʏ': [
                            {'IPA': 'y', "classes": ["vowels"], 'types': ['close', 'front', 'rounded'], 'rules': []},
                            {'IPA': 'ʉ', "classes": ["vowels"], 'types': ['close', 'central', 'rounded'], 'rules': []}], 
                        'ʊ': [
                            {'IPA': 'ʉ', "classes": ["vowels"], 'types': ['close', 'central', 'rounded'], 'rules': []}, 
                            {'IPA': 'u', "classes": ["vowels"], 'types': ['close', 'back', 'rounded'], 'rules': []}],
                        'ɐ': [
                            {'IPA': 'æ', "classes": ["vowels"], 'types': ['near-open', 'front', 'unrounded'], 'rules': []},
                            {'IPA': 'ɑ', "classes": ["vowels"], 'types': ['open', 'back', 'unrounded'], 'rules': []}]
                      }


# Transfor the vowel's roundedness when there is a comparable sound available
def vowel_roundness(word, rules=roundness_rules, unround=False):

    change_type_1 = "unrounded" if not unround else "rounded"
    change_type_2 = "rounded" if not unround else "unrounded"
    rounding_rule = "rounding" if not unround else "unrounding"
    
    for i, syllable in enumerate(word["syllables"]):
        for j, sound in enumerate(syllable["sounds"]):
            indexes = (i, j)

            if not sound_validation.sound_rule_main_distributor(rules[rounding_rule], indexes, word):
                continue            
            
            if change_type_1 in sound["types"]:
                new_sound_types = sound["types"].copy()
                new_sound_types.remove(change_type_1)
                new_sound_types.append(change_type_2)
                for new_sound in sounds_list:
                    if set(new_sound["types"]) == set(new_sound_types):
                        syllable["sounds"][j] = new_sound
                        break

        word["syllables"][i]["syllable"] = "".join(IPA["IPA"] for IPA in syllable["sounds"])

    return word


# Shift the vowel forward of backward
def vowel_fronting(rules, word, fronting=True, strong=False):

    direction = "fronting" if fronting else "rearing"
    step = -2 if strong else -1
    step *= -1 if not fronting else 1
    
    for i, syllable in enumerate(word["syllables"]):
        for j, sound in enumerate(syllable["sounds"]):
            if "vowels" in sound["classes"]:
                indexes = (i, j)

                if not sound_validation.sound_rule_main_distributor(rules[direction], indexes, word):
                    continue

                matching = set(sound["types"]) & set(fronting_variables)
                if matching == set() or sound["IPA"] == 'ɐ':
                    fronting_exceptions[sound["IPA"]]
                    step = 0 if fronting else 1
                    syllable["sounds"][j] = fronting_exceptions[sound["IPA"]][step]
                    continue
                vowel_place = fronting_variables.index(list(matching)[0])
                new_vowel_place = vowel_place + step
                if new_vowel_place < 0:
                    new_vowel_place = 0
                if new_vowel_place > 2:
                    new_vowel_place = 2
                sound["types"].remove(fronting_variables[vowel_place])
                new_sound_types = sound["types"] + [fronting_variables[new_vowel_place]]
                for new_sound in sounds_list:
                    if set(new_sound["types"]) == set(new_sound_types):
                        syllable["sounds"][j] = new_sound
                        break

            word["syllables"][i]["syllable"] = "".join(IPA["IPA"] for IPA in syllable["sounds"])

        return word

if __name__ == "__main__":
    pass