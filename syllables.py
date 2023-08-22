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
        syllable_dict = {"stress": None, "syllable": "", "sounds": [], "legal": None}

        syllable_dict["sounds"] = list_of_sounds
        syllable_dict["syllable"] = "".join(sound["IPA"] for sound in list_of_sounds)
        
        if any(sound in vowel_sounds for sound in syllable_dict["sounds"]):
            syllable_dict["legal"] = True
        else:
            syllable_dict["legal"] = False

        return syllable_dict

    except:
        return None


def redefine_more_than_one_syllables(list_of_syllables = None):
    # The function receives a pair of syllables (syntax in README.md)
    # The function checks that each syllable is contains a vowel sound (making it legal)
    # If the syllable is 
    # If a list contains no legal syllables, the function returns "None"
    # The function combines adds the illegal syllable (or parts of it) to the legal syllable if the combination is allowed

    if list_of_syllables is None:
        return None
    
    try:
        legal_indexes = []
        illegal_indexes = []

        for i, syll in enumerate(list_of_syllables):
            if syll['legal']:
                legal_indexes.append(i)
            else:
                illegal_indexes.append(i)

        if not legal_indexes:
            return None

        for j in illegal_indexes:
            illegal_sounds = list_of_syllables[j]["sounds"]
            not_combined = True
            for k in legal_indexes:
                for a in range(len(list_of_syllables)):
                    if k+a == j and not_combined:
                        # Add illegal sound in after a legal syllable
                        target_syllable = list_of_syllables[k]
                        rules.analyze_rules(target_syllable, illegal_sounds)
                        target_syllable["sounds"].extend(illegal_sounds)
                        list_of_syllables[k]["syllable"] += "".join(IPA["IPA"] for IPA in illegal_sounds)
                        not_combined = False
                    elif k-a == j and not_combined:
                        # Add illegal sound in front of a legal syllable
                        target_syllable = list_of_syllables[k]
                        rules.analyze_rules(illegal_sounds, target_syllable, False)
                        original_sounds = target_syllable["sounds"]
                        target_syllable["sounds"] = illegal_sounds + original_sounds
                        list_of_syllables[k]["syllable"] = "".join(IPA["IPA"] for IPA in illegal_sounds) + target_syllable["syllable"]
                        not_combined = False


        list_of_syllables = [syll for i, syll in enumerate(list_of_syllables) if i not in illegal_indexes]

        return list_of_syllables
    except:
        return None


def return_rules(list_of_sounds):
    return None

if __name__ == "__main__":
    pass