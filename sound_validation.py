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


def sound_itself_validity_check(sound_itself_rules, sound):
    for category in sound_itself_rules:
        if checker_map.get(category)(sound[category], sound_itself_rules[category]):
            return True
    return False   


def after_sound_validity_check(after_sound_rules, indexes, word):
    i, j = indexes
    if i == 0 and j == 0:
        return False

    t_j = j - 1
    t_i = i - 1 if t_j < 0 else i
    sound_after_rules = word["syllables"][t_i]["sounds"][t_j]

    for after_types in after_sound_rules:
        if checker_map.get(after_types)(sound_after_rules[after_types], after_sound_rules[after_types]):
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

    sound_categories = word["syllables"][b_i]["sounds"][b_j]

    for category in before_rule:
        if checker_map.get(category)(sound_categories[category], before_rule[category]):
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