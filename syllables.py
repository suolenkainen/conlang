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
    # The function receives a list of syllables (syntax in README.md)
    # If a list contains no legal syllables, the function returns "None"
    # Each syllable is assigned to an index and they are divided into legal and illegal lists
    # Illegal syllable is added to a legal syllable if it is allowed
    # If an illegal syllable is split, it can be added to the following syllable, otherwise it is lost.

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
                        not_combined = False
                        # Add illegal sound in after a legal syllable
                        target_syllable = list_of_syllables[k]
                        valid_sounds, remaining_sounds = rules.analyze_rules(illegal_sounds, target_syllable)
                        if remaining_sounds:
                            not_combined = True
                            illegal_sounds = remaining_sounds
                        target_syllable["sounds"].extend(valid_sounds)
                        list_of_syllables[k]["syllable"] += "".join(IPA["IPA"] for IPA in valid_sounds)
                    if k-a == j and not_combined:
                        not_combined = False
                        # Add illegal sound in front of a legal syllable
                        target_syllable = list_of_syllables[k]
                        valid_sounds, remaining_sounds = rules.analyze_rules(illegal_sounds, target_syllable, False)
                        original_sounds = target_syllable["sounds"]
                        target_syllable["sounds"] = valid_sounds + original_sounds
                        list_of_syllables[k]["syllable"] = "".join(IPA["IPA"] for IPA in valid_sounds) + target_syllable["syllable"]


        list_of_syllables = [syll for i, syll in enumerate(list_of_syllables) if i not in illegal_indexes]

        return list_of_syllables
    except:
        return None


def return_rules(list_of_sounds):
    return None

if __name__ == "__main__":
    pass