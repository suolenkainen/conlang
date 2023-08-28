#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/conlang


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
    "classes": classes}


def sound_rule_main_distributor(rules, indexes, word):


    for category in rules:
        if validity_checker_map.get(category)(rules[category], indexes, word):
            return True
    
    return True

def sound_itself_validity_check(sound_itself_rules, indexes, word):
    i, j = indexes
    sound = word["syllables"][i]["sounds"][j]
    rules = sound_itself_rules

    for category in rules:
        if checker_map.get(category)(sound[category], rules[category]):
            return True
    return False   


def after_sound_validity_check(after_sound_rules, indexes, word):
    i, j = indexes
    if i == 0 and j == 0:
        return False

    t_j = j - 1
    t_i = i - 1 if t_j < 0 else i
    sound = word["syllables"][t_i]["sounds"][t_j]
    rules = after_sound_rules

    for category in rules:
        if checker_map.get(category)(sound[category], rules[category]):
            return True
    return False


def before_sound_validity_check(before_rule, indexes, word):
    i, j = indexes
    syllable_count = len(word["syllables"])
    sound_count = len(word["syllables"][i]["sounds"])

    b_j = (j + 1) % sound_count
    b_i = i + 1 if j >= sound_count - 1 else i
    
    if b_j == 0 and i >= syllable_count -1:
        return False

    sound = word["syllables"][b_i]["sounds"][b_j]
    rules = before_rule

    for category in rules:
        if checker_map.get(category)(sound[category], rules[category]):
            return True
    return False   


def between_sounds_validity_check(between_rules, indexes, word):
    i, j = indexes
    syllable_count = len(word["syllables"])
    sound_count = len(word["syllables"][i]["sounds"])

    if (i, j) == (0, 0) or (i >= syllable_count - 1 and j >= sound_count - 1):
        return False

    if after_sound_validity_check(between_rules["preceeding"], indexes, word):
        if before_sound_validity_check(between_rules["trailing"], indexes, word):
            return True
    return False   


validity_checker_map = {
    "sound itself": sound_itself_validity_check,
    "after sound":  after_sound_validity_check,
    "between": between_sounds_validity_check,
    "before": before_sound_validity_check
}


if __name__ == "__main__":
    pass