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

# Utility functions based on required check
class Utility_Checkers:
    
    @staticmethod
    def IPA(sound_IPA, IPA_list):
        if sound_IPA in IPA_list:
            return True
        return False
    
    @staticmethod
    def types(types, type_rules):
        # tarkistetaan niin, että onko säännön lista
        for rule in type_rules:
            matching = set(rule) & set(types)
            if sorted(list(matching)) == sorted(rule):
                return True
        return False

    @staticmethod
    def classes(classes, rules):
        print(classes, rules)

def vowel_roundness(word, rules=roundness_rules, unround=False):

    change_type_1 = "unrounded" if not unround else "rounded"
    change_type_2 = "rounded" if not unround else "unrounded"
    rounding_rule = "rounding" if not unround else "unrounding"
    
    for i, syllable in enumerate(word["syllables"]):
        for j, sound in enumerate(syllable["sounds"]):
            indexes = (i, j)
            if "IPA match" in rules[rounding_rule] and IPA_validity_check(rules[rounding_rule], sound["IPA"]):
                pass 
            elif "after sound" in rules[rounding_rule] and after_type_class_validity_check(rules[rounding_rule], indexes, word):
                pass 
            elif "between" in rules[rounding_rule] and between_types_validity_check(rules[rounding_rule], indexes, word):
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


def IPA_validity_check(rules, sound):
    categories = rules["IPA match"]
    if getattr(Utility_Checkers, "IPA")(sound["IPA"], categories["IPA"]):
        return True
    return False   


def types_validity_check(rules, indexes, word):
    i, j = indexes
    types_list = rules["types"]
    if getattr(Utility_Checkers, "types")(word["syllables"][i]["sounds"][j]["types"], types_list):
        return True
    return False 


def after_type_class_validity_check(rules, indexes, word):
    i, j = indexes
    if i == 0 and j == 0:
        return False

    after_types = rules["after sound"]
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

    after_categories = rules["between"]
    p_j = j - 1
    p_i = i - 1 if p_j < 0 else i
    t_j = j + 1
    t_i = i

    if j >= sound_count - 1:
        t_j = 0
        t_i += 1

    preceeding_categories = word["syllables"][p_i]["sounds"][p_j]
    trailing_categories = word["syllables"][t_i]["sounds"][t_j]

    for pre_category in after_categories["preceeding"]:
        if getattr(Utility_Checkers, pre_category)(preceeding_categories[pre_category], after_categories["preceeding"][pre_category]):
            for trail_category in after_categories["trailing"]:
                if getattr(Utility_Checkers, trail_category)(trailing_categories[trail_category], after_categories["trailing"][trail_category]):
                    return True            
    return False   



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