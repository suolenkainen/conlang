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
closing_variables = rules_list["vowels"]["closing variables"]
fronting_variables = rules_list["vowels"]["fronting variables"]

fronting_exceptions = {"ɪ": ["i", "ɨ"], "ʏ": ["y", "ʉ"], "ʊ": ["ʉ", "u"], "ɐ": ["æ", "ɑ"]}
closing_exceptions = {'ɪ': ['i', 'e'], 'ʏ': ['y', 'ø'], 'ʊ': ['u', 'o'], 'ɐ': ['ɜ', 'ä'], 'ə': ['ɘ', 'ɜ']}
exception_categories = [fronting_exceptions, closing_exceptions]

for exceptions_list in exception_categories:
    for exception in exceptions_list:
        for sound in sounds_list["vowels"]:
            if exceptions_list[exception][0] == sound["IPA"]: exceptions_list[exception][0] = sound
            if exceptions_list[exception][1] == sound["IPA"]: exceptions_list[exception][1] = sound


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
                    step = 0 if fronting else 1
                    syllable["sounds"][j] = fronting_exceptions[sound["IPA"]][step]
                
                else:
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


def vowel_closing(rules, word, closing=True, strong=False):
    
    direction = "closing" if closing else "opening"
    step = -2 if strong else -1
    step *= -1 if not closing else 1

    for i, syllable in enumerate(word["syllables"]):
        for j, sound in enumerate(syllable["sounds"]):
            if "vowels" in sound["classes"]:
                indexes = (i, j)

                if not sound_validation.sound_rule_main_distributor(rules[direction], indexes, word):
                    continue

                matching = set(sound["types"]) & set(closing_variables)

                if sound["IPA"] in closing_exceptions:
                    step = 0 if closing else 1
                    syllable["sounds"][j] = closing_exceptions[sound["IPA"]][step]

                else:
                    vowel_place = closing_variables.index(list(matching)[0])
                    new_vowel_place = vowel_place + step
                    if new_vowel_place < 0:
                        new_vowel_place = 0
                    if new_vowel_place > 6:
                        new_vowel_place = 6

                    found = False
                    new_sound_types = sound["types"].copy()

                    while not found:
                        new_sound_types.remove(closing_variables[vowel_place])
                        vowel_place = new_vowel_place
                        new_sound_types = new_sound_types + [closing_variables[vowel_place]]
                        for new_sound in sounds_list:
                            if set(new_sound["types"]) == set(new_sound_types):
                                syllable["sounds"][j] = new_sound
                                found = True
                                break
                        new_vowel_place = vowel_place + step

            word["syllables"][i]["syllable"] = "".join(IPA["IPA"] for IPA in syllable["sounds"])

    return word


if __name__ == "__main__":
    pass