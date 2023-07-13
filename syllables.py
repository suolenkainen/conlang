#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/conlang

from sounds import consonants as C, vowels as V

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
    if list_of_syllables == []:
        return None
    
    try:
        list_of_syllables.extend([])
        return list_of_syllables
    except:
        return None



if __name__ == "__main__":
    pass