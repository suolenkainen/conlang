#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/conlang

# from sounds import consonants as consonant_sounds, vowels as vowel_sounds
import json
import rules

sound_file_path = 'sounds.json'
with open(sound_file_path, 'r') as sound_file:
    sound_data = sound_file.read()
    sound_data_dict = json.loads(sound_data)
    vowel_sounds = sound_data_dict["vowels"]
    consonant_sounds = sound_data_dict["consonants"]

def combine_sounds_to_syllable(list_of_sounds = []):
    if list_of_sounds == []:
        return None
    
    try:
        syllable_dict = {"stress": None, "syllable": "", "sounds": []}

        syllable_dict["sounds"] = list_of_sounds
        syllable_dict["syllable"] = "".join(sound["IPA"] for sound in list_of_sounds)

        return syllable_dict

    except:
        return None


def redefine_more_than_one_syllables(list_of_syllables = None):

    if list_of_syllables is None:
        return None
    
    try:
        legal_indexes = []
        illegal_indexes = []

        for i, syll in enumerate(list_of_syllables):
            has_vowel = any(sound in vowel_sounds for sound in syll["sounds"])
            if has_vowel:
                legal_indexes.append(i)
            else:
                illegal_indexes.append(i)

        if not legal_indexes:
            return list_of_syllables

        for j in illegal_indexes:
            illegal_sounds = list_of_syllables[j]["sounds"]
            for ill in illegal_sounds:
                ill["rules"]= rules.illegal_clusters()
            for k in legal_indexes:
                for a in range(len(list_of_syllables)):
                    if k+a == j:
                        list_of_syllables[k]["sounds"].extend(illegal_sounds)
                        list_of_syllables[k]["syllable"] += "".join(IPA["IPA"] for IPA in illegal_sounds)

                    elif k-a == j:
                        original_sounds = list_of_syllables[k]["sounds"]
                        list_of_syllables[k]["sounds"] = illegal_sounds + original_sounds
                        list_of_syllables[k]["syllable"] = "".join(IPA["IPA"] for IPA in illegal_sounds) + list_of_syllables[k]["syllable"]


        list_of_syllables = [syll for i, syll in enumerate(list_of_syllables) if i not in illegal_indexes]

        return list_of_syllables
    except:
        return None

def return_rules(list_of_sounds):
    return None

if __name__ == "__main__":
    pass