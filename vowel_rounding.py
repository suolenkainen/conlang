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


def IPA(sound_IPA, IPA_list):
    if sound_IPA in IPA_list:
        return True
    return False

def types(types, type_rules):
    for rule in type_rules:
        matching = set(rule) & set(types)
        if sorted(list(matching)) == sorted(rule):
            return True
    return False

def classes(classes, class_rules):
    for rule in class_rules:
        matching = set(rule) & set(classes)
        if sorted(list(matching)) == sorted(rule):
            return True
    return False

checker_map = {
    "IPA": IPA,
    "types": types,
    "classes": classes
}

def vowel_roundness(word, rules=roundness_rules, unround=False):

    change_type_1 = "unrounded" if not unround else "rounded"
    change_type_2 = "rounded" if not unround else "unrounded"
    rounding_rule = "rounding" if not unround else "unrounding"
    
    for i, syllable in enumerate(word["syllables"]):
        for j, sound in enumerate(syllable["sounds"]):
            indexes = (i, j)
            if "sound itself" in rules[rounding_rule] and sound_itself_validity_check(rules[rounding_rule], sound):
                pass 
            elif "after sound" in rules[rounding_rule] and after_sound_validity_check(rules[rounding_rule], indexes, word):
                pass 
            elif "between" in rules[rounding_rule] and between_sounds_validity_check(rules[rounding_rule], indexes, word):
                pass
            elif "before" in rules[rounding_rule] and before_sound_validity_check(rules[rounding_rule], indexes, word):
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


def sound_itself_validity_check(rules, sound):
    categories = rules["sound itself"]
    for category in categories:
        if checker_map.get(category)(sound[category], categories[category]):
            return True
    return False   


def after_sound_validity_check(rules, indexes, word):
    i, j = indexes
    if i == 0 and j == 0:
        return False

    t_j = j - 1
    t_i = i - 1 if t_j < 0 else i
    sound_after_rules = word["syllables"][t_i]["sounds"][t_j]

    for after_types in rules["after sound"]:
        if checker_map.get(after_types)(sound_after_rules[after_types], rules["after sound"][after_types]):
            return True
    return False


def before_sound_validity_check(rules, indexes, word):
    i, j = indexes
    syllable_count = len(word["syllables"])
    sound_count = len(word["syllables"][i]["sounds"])

    rule_categories = rules["before"]
    b_j = (j + 1) % sound_count
    b_i = i + 1 if j >= sound_count - 1 else i
    
    if b_j == 0 and i >= syllable_count -1:
        return False

    sound_categories = word["syllables"][b_i]["sounds"][b_j]

    for category in rule_categories:
        if checker_map.get(category)(sound_categories[category], rule_categories[category]):
            return True
    return False   


def between_sounds_validity_check(rules, indexes, word):
    i, j = indexes
    syllable_count = len(word["syllables"])
    sound_count = len(word["syllables"][i]["sounds"])

    if (i, j) == (0, 0) or (i >= syllable_count - 1 and j >= sound_count - 1):
        return False

    after_categories = rules["between"]
    p_j = j - 1
    p_i = i - 1 if p_j < 0 else i
    t_j = (j + 1) % sound_count
    t_i = i + 1 if j >= sound_count - 1 else i

    preceeding_categories = word["syllables"][p_i]["sounds"][p_j]
    trailing_categories = word["syllables"][t_i]["sounds"][t_j]

    for pre_category in after_categories["preceeding"]:
        if checker_map.get(pre_category)(preceeding_categories[pre_category], after_categories["preceeding"][pre_category]):
            for trail_category in after_categories["trailing"]:
                if checker_map.get(trail_category)(trailing_categories[trail_category], after_categories["trailing"][trail_category]):
                    return True
    return False   


if __name__ == "__main__":
    pass