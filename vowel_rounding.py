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


def vowel_roundness(word, rules=roundness_rules, unround=False):

    change_type_1 = "unrounded" if not unround else "rounded"
    change_type_2 = "rounded" if not unround else "unrounded"
    rounding_rule = "rounding" if not unround else "unrounding"
    
    for i, syllable in enumerate(word["syllables"]):
        for j, sound in enumerate(syllable["sounds"]):
            indexes = (i, j)
            if "sound itself" in rules[rounding_rule] and sound_validation.sound_itself_validity_check(rules[rounding_rule]["sound itself"], sound):
                pass 
            elif "after sound" in rules[rounding_rule] and sound_validation.after_sound_validity_check(rules[rounding_rule]["after sound"], indexes, word):
                pass 
            elif "between" in rules[rounding_rule] and sound_validation.between_sounds_validity_check(rules[rounding_rule]["between"], indexes, word):
                pass
            elif "before" in rules[rounding_rule] and sound_validation.before_sound_validity_check(rules[rounding_rule]["before"], indexes, word):
                pass
            else:
                continue
            
            if change_type_1 in sound["types"]: ### Tän ei pitäis olla se 
                new_sound_types = sound["types"].copy()
                new_sound_types.remove(change_type_1)
                new_sound_types.append(change_type_2)
                for new_sound in sounds_list:
                    if new_sound["types"] == new_sound_types:
                        syllable["sounds"][j] = new_sound
                        break

        word["syllables"][i]["syllable"] = "".join(IPA["IPA"] for IPA in syllable["sounds"])

    return word


if __name__ == "__main__":
    pass