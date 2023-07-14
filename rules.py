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



def analyze_rules(transferring_sounds=None, target_syllable=None):
    print(rules_list)
    return transferring_sounds, target_syllable


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

    # for sound_type_list in sounds_list.values():
    #     for sound in sound_type_list:
    #         if sound["rules"]:
    #             print(sound)

    return sounds_list

if __name__ == "__main__":
    set_rules_for_sounds(rules_list, sounds_list)