#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/conlang

import json

file_path = 'rules.json'
with open(file_path, 'r') as file:
    rules_list = json.load(file)
    

file_path = 'sounds.json'
with open(file_path, 'r') as file:
    sounds_list = json.load(file)

roundness_rules = rules_list["vowels"]["roundedness changes"]
dropping_rules = rules_list["vowels"]["dropping"]
moving_rules = rules_list["vowels"]["moving"]
replacement_rules = rules_list["vowels"]["replacement"]
degemination_rules = rules_list["vowels"]["degemination"]



def vowel_roundness(word, rules=roundness_rules, unround=False):

    change_type_1 = "unrounded" if not unround else "rounded"
    change_type_2 = "rounded" if not unround else "unrounded"
    rounding_rule = "rounding" if not unround else "unrounding"
    
    for i, syllable in enumerate(word["syllables"]):
        for j, sound in enumerate(syllable["sounds"]):
            indexes = (i, j)
            if "IPA" in rules[rounding_rule] and IPA_validity_check(rules[rounding_rule], sound["IPA"]):
                pass 
            elif "after types" in rules[rounding_rule] and after_type_class_validity_check(rules[rounding_rule], indexes, word):
                pass 
            elif "between types" in rules[rounding_rule] and between_types_validity_check(rules[rounding_rule], indexes, word):
                pass
            else:
                continue
            
            if change_type_1 in sound["types"]:
                new_sound_types = sound["types"].copy()
                new_sound_types.remove(change_type_1)
                new_sound_types.append(change_type_2)
                for new_sound in sounds_list:
                    if new_sound["types"] == new_sound_types:
                        syllable["sounds"][j] = new_sound
                        break

        word["syllables"][i]["syllable"] = "".join(IPA["IPA"] for IPA in syllable["sounds"])

    return word



def IPA_validity_check(rules, sound_IPA):
    IPA_list = rules["IPA"]
    if sound_IPA in IPA_list:
        return True
    return False


def types_validity_check(rules, indexes, word):
    i, j = indexes
    types_list = rules["types"]
    for types in types_list:
        matching = set(types) & set(word["syllables"][i]["sounds"][j]["types"])
        if len(matching) == 0:
            return False
    
    return True


def after_type_class_validity_check(rules, indexes, word):
    i, j = indexes
    if i == 0 and j == 0:
        return False

    after_types = rules["after types"]
    t_j = j - 1
    t_i = i - 1 if t_j < 0 else i
    after = word["syllables"][t_i]["sounds"][t_j]["types"]

    matching_combination_found = any(
        after in after_types
        for after in after_types
    )

    return matching_combination_found  

def between_types_validity_check(rules, indexes, word):
    i, j = indexes
    syllable_count = len(word["syllables"])
    sound_count = len(word["syllables"][i]["sounds"])

    if i == 0 and j == 0:
         return False
    if i >= syllable_count-1 and j >= sound_count-1: 
        return False

    after_types = rules["between types"]
    p_j = j - 1
    p_i = i - 1 if p_j < 0 else i
    t_j = j + 1
    t_i = i

    if j >= sound_count - 1:
        t_j = 0
        t_i += 1

    preceeding_types = word["syllables"][p_i]["sounds"][p_j]["types"]
    trailing_types = word["syllables"][t_i]["sounds"][t_j]["types"]

    matching_combination_found = any(
        preceding in preceeding_types and trailing in trailing_types
        for preceding in after_types["preceeding"]
        for trailing in after_types["trailing"]
    )

    return matching_combination_found    


def vowel_drop(word, rules=dropping_rules):
    dropping_rules
    pass


def move_front_back(word, rules=moving_rules):
    moving_rules


def move_high_low(word, rules=moving_rules):
    moving_rules


def vowel_replacement(word, rules=replacement_rules):
    replacement_rules


def vowel_degemination(word, rules=degemination_rules):
    degemination_rules


if __name__ == "__main__":
    pass