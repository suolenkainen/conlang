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



def analyze_rules(transferring_sounds, target_syllable, append_to_syllable=True):

    if not transferring_sounds or not target_syllable:
        return transferring_sounds, target_syllable
    
    if append_to_syllable:
        adjecent_appending_sound = transferring_sounds[-1]
        adjecent_trailing_sound = target_syllable["sounds"][0]
    else:
        adjecent_appending_sound = transferring_sounds[0]
        adjecent_trailing_sound = target_syllable["sounds"][-1]

    if adjecent_appending_sound["rules"] == []:
        return transferring_sounds, []

    non_violation = True

    for rule in adjecent_appending_sound["rules"]:
        if "clusters" in rule:
            non_violation = analyze_cluster_rules(adjecent_appending_sound, adjecent_trailing_sound, rule)

    if not non_violation:
        return [], transferring_sounds
        
    return transferring_sounds, []


def analyze_cluster_rules(appending_sound, trailing_sound, rule):
    if not appending_sound or not trailing_sound or not rule:
        return None
    
    appending_IPA = appending_sound["IPA"]
    trailing_IPA = trailing_sound["IPA"]

    if "illegal clusters" in rule["clusters"]:
        for cluster in rule["clusters"]["illegal clusters"]:
            if cluster == [appending_IPA, trailing_IPA]:
                return False

    return True


# Tää on jotenkin outo
def set_rules_for_sounds(rules_list=None, sounds_list=None):
    if rules_list is None or sounds_list is None:
        return None

    for ruletype, rulesets in rules_list.items():
        for ruleset, rules in rulesets.items():
            for rule in rules:
                for soundtype in sounds_list:
                    for sound in sounds_list[soundtype]:
                        if sound["IPA"] in rule:
                            if ruletype not in sound["rules"]:
                                sound["rules"].append({ruletype: {}})
                            if ruleset not in sound["rules"][-1]:
                                sound["rules"][-1][ruletype] = {ruleset: []}
                            if rule not in sound["rules"][-1][ruletype][ruleset]:
                                sound["rules"][-1][ruletype][ruleset].append(rule)

    return sounds_list

if __name__ == "__main__":
    pass