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


def vowel_roundness(word, rules=roundness_rules, unround=False):

    change_type_1 = "unrounded"
    change_type_2 = "rounded"
    if unround:
        change_type_1 = "rounded"
        change_type_2 = "unrounded"

    for i, syllable in enumerate(word["syllables"]):
        for j, sound in enumerate(syllable["sounds"]):
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


def vowel_drop(word, rules=dropping_rules):
    dropping_rules
    pass


# Lisää tämä syllables.py tiedostoon
def rewrite_syllable(syllable):
    syllable["syllable"] = "".join(IPA["IPA"] for IPA in syllable["sounds"])
    return syllable

if __name__ == "__main__":
    pass