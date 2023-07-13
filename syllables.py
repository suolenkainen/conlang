#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/conlang

from sounds import consonants as C, vowels as vowel_sounds

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


def redefine_more_than_one_syllables(list_of_syllables = []):
    # When a syllable comes in that has no vowel, it is merged to a syllable next to it.

    if list_of_syllables == []:
        return None
    
    try:
        list_of_syllables.extend([])

        legal_indexes = []
        illegal_indexes = []

        for i, syll in enumerate(list_of_syllables):
            has_vowel = False
            for sound in syll["sounds"]:
                if sound in vowel_sounds:
                    has_vowel = True
                    break
            
            if has_vowel:
                legal_indexes.append(i)
            else:
                illegal_indexes.append(i)

        if legal_indexes == []:
            return list_of_syllables

        for j in illegal_indexes:
            illegal_sounds = list_of_syllables[j]["sounds"]
            for k in legal_indexes:
                for a in range(len(list_of_syllables)):
                    if k+a == j:
                        list_of_syllables[k]["sounds"].extend(illegal_sounds)
                        syllable = list_of_syllables[k]["syllable"]
                        list_of_syllables[k]["syllable"] = syllable + "".join(IPA["IPA"] for IPA in illegal_sounds)
                        break
                    elif k-a == j:
                        original_sounds = list_of_syllables[k]["sounds"]
                        list_of_syllables[k]["sounds"] = illegal_sounds + original_sounds
                        syllable = list_of_syllables[k]["syllable"]
                        list_of_syllables[k]["syllable"] = "".join(IPA["IPA"] for IPA in illegal_sounds) + syllable
                        break
                    
        for j in reversed(illegal_indexes):
            list_of_syllables.pop(j)

        return list_of_syllables
    except:
        return None



if __name__ == "__main__":
    pass