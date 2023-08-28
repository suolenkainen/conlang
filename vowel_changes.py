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

# validity_checker_map = {
#     "sound itself": sound_validation.sound_itself_validity_check,
#     "after sound":  sound_validation.after_sound_validity_check,
#     "between": sound_validation.between_sounds_validity_check,
#     "before": sound_validation.before_sound_validity_check
# }

def vowel_roundness(word, rules=roundness_rules, unround=False):

    change_type_1 = "unrounded" if not unround else "rounded"
    change_type_2 = "rounded" if not unround else "unrounded"
    rounding_rule = "rounding" if not unround else "unrounding"
    
    for i, syllable in enumerate(word["syllables"]):
        for j, sound in enumerate(syllable["sounds"]):
            indexes = (i, j)

            if "sound itself" in rules[rounding_rule] and sound_validation.sound_itself_validity_check(rules[rounding_rule]["sound itself"], indexes, word):
                pass 
            elif "after sound" in rules[rounding_rule] and sound_validation.after_sound_validity_check(rules[rounding_rule]["after sound"], indexes, word):
                pass 
            elif "between" in rules[rounding_rule] and sound_validation.between_sounds_validity_check(rules[rounding_rule]["between"], indexes, word):
                pass
            elif "before" in rules[rounding_rule] and sound_validation.before_sound_validity_check(rules[rounding_rule]["before"], indexes, word):
                pass
            else:
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


def vowel_fronting(rules, word, fronting=True, strong=False):

    direction = "fronting" if fronting else "rearing"
    step = -2 if strong else -1
    step *= -1 if not fronting else 1
    
    for i, syllable in enumerate(word["syllables"]):
        for j, sound in enumerate(syllable["sounds"]):
            if "vowels" in sound["classes"]:
                indexes = (i, j)
                    
                if "sound itself" in rules[direction] and sound_validation.sound_itself_validity_check(rules[direction]["sound itself"], indexes, word):
                    pass 
                elif "after sound" in rules[direction] and sound_validation.after_sound_validity_check(rules[direction]["after sound"], indexes, word):
                    pass 
                elif "between" in rules[direction] and sound_validation.between_sounds_validity_check(rules[direction]["between"], indexes, word):
                    pass
                elif "before" in rules[direction] and sound_validation.before_sound_validity_check(rules[direction]["before"], indexes, word):
                    pass
                else:
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