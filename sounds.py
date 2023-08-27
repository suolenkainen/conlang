#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/conlang

# Prime system by having all the letters
# This file is to update the sounds.json and serves to other purpose

import json

vowels = []
consonants = []

""" All vowel sounds """
vowels.append({'IPA': 'i', "classes": ["vowels"], 'types': ['close', 'front', 'unrounded'], 'rules': []})
vowels.append({'IPA': 'y', "classes": ["vowels"], 'types': ['close', 'front', 'rounded'], 'rules': []})
vowels.append({'IPA': 'ɨ', "classes": ["vowels"], 'types': ['close', 'central', 'unrounded'], 'rules': []})
vowels.append({'IPA': 'ʉ', "classes": ["vowels"], 'types': ['close', 'central', 'rounded'], 'rules': []}) 
vowels.append({'IPA': 'ɯ', "classes": ["vowels"], 'types': ['close','back','unrounded'], 'rules': []}) 
vowels.append({'IPA': 'u', "classes": ["vowels"], 'types': ['close', 'back', 'rounded'], 'rules': []})
vowels.append({'IPA': 'ɪ', "classes": ["vowels"], 'types': ['near-close', 'near-front', 'unrounded'], 'rules': []})
vowels.append({'IPA': 'ʏ', "classes": ["vowels"], 'types': ['near-close', 'near-front', 'rounded'], 'rules': []})
vowels.append({'IPA': 'ʊ', "classes": ["vowels"], 'types': ['near-close', 'near-back', 'rounded'], 'rules': []})
vowels.append({'IPA': 'e', "classes": ["vowels"], 'types': ['close-mid', 'front', 'unrounded'], 'rules': []})
vowels.append({'IPA': 'ø', "classes": ["vowels"], 'types': ['close-mid', 'front', 'rounded'], 'rules': []})
vowels.append({'IPA': 'ɘ', "classes": ["vowels"], 'types': ['close-mid', 'central', 'unrounded'], 'rules': []})
vowels.append({'IPA': 'ɵ', "classes": ["vowels"], 'types': ['close-mid', 'central', 'rounded'], 'rules': []})
vowels.append({'IPA': 'ɤ', "classes": ["vowels"], 'types': ['close-mid', 'back', 'unrounded'], 'rules': []})
vowels.append({'IPA': 'o', "classes": ["vowels"], 'types': ['close-mid', 'back', 'rounded'], 'rules': []})
vowels.append({'IPA': 'e̞', "classes": ["vowels"], 'types': ['mid', 'front', 'unrounded'], 'rules': []})
vowels.append({'IPA': 'ø̞', "classes": ["vowels"], 'types': ['mid', 'front', 'rounded'], 'rules': []})
vowels.append({'IPA': 'ə', "classes": ["vowels"], 'types': ['mid', 'central', 'unrounded'], 'rules': []})
vowels.append({'IPA': 'ɤ̞', "classes": ["vowels"], 'types': ['mid', 'back', 'unrounded'], 'rules': []})
vowels.append({'IPA': 'o̞', "classes": ["vowels"], 'types': ['mid', 'back', 'rounded'], 'rules': []})
vowels.append({'IPA': 'œ', "classes": ["vowels"], 'types': ['mid', 'front', 'rounded'], 'rules': []})
vowels.append({'IPA': 'ɛ', "classes": ["vowels"], 'types': ['open-mid', 'front', 'unrounded'], 'rules': []})
vowels.append({'IPA': 'ɜ', "classes": ["vowels"], 'types': ['open-mid', 'central', 'unrounded'], 'rules': []})
vowels.append({'IPA': 'ɞ', "classes": ["vowels"], 'types': ['open-mid', 'central', 'rounded'], 'rules': []})
vowels.append({'IPA': 'ʌ', "classes": ["vowels"], 'types': ['open-mid', 'back', 'unrounded','low'], 'rules': []})
vowels.append({'IPA': 'ɔ', "classes": ["vowels"], 'types': ['open-mid', 'back', 'rounded'], 'rules': []})
vowels.append({'IPA': 'æ', "classes": ["vowels"], 'types': ['near-open', 'front', 'unrounded'], 'rules': []})
vowels.append({'IPA': 'ɐ', "classes": ["vowels"], 'types': ['near-open', 'central'], 'rules': []})
vowels.append({'IPA': 'a', "classes": ["vowels"], 'types': ['open', 'front', 'unrounded'], 'rules': []})
vowels.append({'IPA': 'ɶ', "classes": ["vowels"], 'types': ['open', 'front', 'rounded'], 'rules': []})
vowels.append({'IPA': 'ä', "classes": ["vowels"], 'types': ['open', 'central', 'unrounded'], 'rules': []}) 
vowels.append({'IPA': 'ɑ', "classes": ["vowels"], 'types': ['open', 'back', 'unrounded'], 'rules': []})
vowels.append({'IPA': 'ɒ', "classes": ["vowels"], 'types': ['open', 'back', 'rounded'], 'rules': []})


""" All nasal sounds"""
consonants.append({'IPA': 'm̥', 'classes': ["nasals", "occlusives"], 'types': ['voiceless','frontcon','bilabial'], 'rules': []})
consonants.append({'IPA': 'm', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','bilabial'], 'rules': []})
consonants.append({'IPA': 'ɱ', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','labiodental'], 'rules': []})
consonants.append({'IPA': 'n̼', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','linguodental'], 'rules': []})
consonants.append({'IPA': 'n̥', 'classes': ["nasals", "occlusives"], 'types': ['voiceless','frontcon','alveloar'], 'rules': []})
consonants.append({'IPA': 'n', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','alveloar'], 'rules': []})
consonants.append({'IPA': 'ɳ̊', 'classes': ["nasals", "occlusives"], 'types': ['voiceless','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'ɳ', 'classes': ["nasals", "occlusives"], 'types': ['voiced','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'ɲ̊', 'classes': ["nasals", "occlusives"], 'types': ['voiceless','backcon','palatal'], 'rules': []})
consonants.append({'IPA': 'ɲ', 'classes': ["nasals", "occlusives"], 'types': ['voiced','backcon','palatal'], 'rules': []})
consonants.append({'IPA': 'ŋ̊', 'classes': ["nasals", "occlusives"], 'types': ['voiceless','backcon','velar'], 'rules': []})
consonants.append({'IPA': 'ŋ', 'classes': ["nasals", "occlusives"], 'types': ['voiced','backcon','velar'], 'rules': []})
consonants.append({'IPA': 'ɴ', 'classes': ["nasals", "occlusives"], 'types': ['voiced','backcon','uvular'], 'rules': []})


""" All Plosives"""
consonants.append({'IPA': 'p', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','frontcon','bilabial'], 'rules': []})
consonants.append({'IPA': 'b', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiced','frontcon','bilabial'], 'rules': []})
consonants.append({'IPA': 'p̪', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiced','frontcon','labiodental'], 'rules': []})
consonants.append({'IPA': 'b̪', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiced','frontcon','labiodental'], 'rules': []})
consonants.append({'IPA': 't̼', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','frontcon','linguolabial'], 'rules': []})
consonants.append({'IPA': 'd̼', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiced','frontcon','linguolabial'], 'rules': []})
consonants.append({'IPA': 't', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 'd', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiced','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 'ʈ', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'ɖ', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiced','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'c', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','palatal'], 'rules': []})
consonants.append({'IPA': 'ɟ', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiced','backcon','palatal'], 'rules': []})
consonants.append({'IPA': 'k', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','velar'], 'rules': []})
consonants.append({'IPA': 'ɡ', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiced','backcon','velar'], 'rules': []})
consonants.append({'IPA': 'q', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','uvular'], 'rules': []})
consonants.append({'IPA': 'ɢ', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiced','backcon','uvular'], 'rules': []})
consonants.append({'IPA': 'ʡ', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','pharyngeal'], 'rules': []})
consonants.append({'IPA': 'ʔ', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiceless','backcon','glottal'], 'rules': []})
consonants.append({'IPA': 'k͡p', 'classes': ["plosives", "occlusives", "obstruents"], 'types': ['voiced','backcon','velar'], 'rules': []})


""" All Affricates"""
consonants.append({'IPA': 'ts', 'classes': ["stridents", "sibilants", "occlusives", "obstruents", "affricates"], 'types': ['voiceless','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 'dz', 'classes': ["stridents", "sibilants", "occlusives", "obstruents", "affricates"], 'types': ['voiced','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 't̠ʃ', 'classes': ["stridents", "sibilants", "occlusives", "obstruents", "affricates"], 'types': ['voiceless','frontcon','postalveolar'], 'rules': []})
consonants.append({'IPA': 'd̠ʒ', 'classes': ["stridents", "sibilants", "occlusives", "obstruents", "affricates"], 'types': ['voiced','frontcon','postalveolar'], 'rules': []})
consonants.append({'IPA': 'ʈʂ', 'classes': ["stridents", "sibilants", "occlusives", "obstruents", "affricates"], 'types': ['voiceless','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'ɖʐ', 'classes': ["stridents", "sibilants", "occlusives", "obstruents", "affricates"], 'types': ['voiced','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'tɕ', 'classes': ["stridents", "sibilants", "occlusives", "obstruents", "affricates"], 'types': ['voiceless','frontcon','palatal'], 'rules': []})
consonants.append({'IPA': 'dʑ', 'classes': ["stridents", "sibilants", "occlusives", "obstruents", "affricates"], 'types': ['voiced','frontcon','palatal'], 'rules': []})
consonants.append({'IPA': 'pɸ', 'classes': ["stridents", "occlusives", "obstruents", "affricates"], 'types': ['voiceless','frontcon','bilabial'], 'rules': []})
consonants.append({'IPA': 'bβ', 'classes': ["stridents", "occlusives", "obstruents", "affricates"], 'types': ['voiced','frontcon','bilabial'], 'rules': []})
consonants.append({'IPA': 'p̪f', 'classes': ["stridents", "occlusives", "obstruents", "affricates"], 'types': ['voiceless','frontcon','labiodental'], 'rules': []})
consonants.append({'IPA': 'b̪v', 'classes': ["stridents", "occlusives", "obstruents", "affricates"], 'types': ['voiced','frontcon','labiodental'], 'rules': []})
consonants.append({'IPA': 't̪θ', 'classes': ["occlusives", "obstruents", "affricates"], 'types': ['voiceless','frontcon','dental'], 'rules': []})
consonants.append({'IPA': 'd̪ð', 'classes': ["occlusives", "obstruents", "affricates"], 'types': ['voiced','frontcon','dental'], 'rules': []})
consonants.append({'IPA': 'tɹ̝̊', 'classes': ["occlusives", "obstruents", "affricates"], 'types': ['voiceless','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 'dɹ̝', 'classes': ["occlusives", "obstruents", "affricates"], 'types': ['voiced','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 't̠ɹ̠̊˔', 'classes': ["occlusives", "obstruents", "affricates"], 'types': ['voiceless','frontcon','postalveolar'], 'rules': []})
consonants.append({'IPA': 'd̠ɹ̠˔', 'classes': ["occlusives", "obstruents", "affricates"], 'types': ['voiced','frontcon','postalveolar'], 'rules': []})
consonants.append({'IPA': 'cç', 'classes': ["occlusives", "obstruents", "affricates"], 'types': ['voiceless','frontcon','palatal'], 'rules': []})
consonants.append({'IPA': 'ɟʝ', 'classes': ["occlusives", "obstruents", "affricates"], 'types': ['voiced','frontcon','palatal'], 'rules': []})
consonants.append({'IPA': 'kx', 'classes': ["occlusives", "obstruents", "affricates"], 'types': ['voiceless','backcon','velar'], 'rules': []})
consonants.append({'IPA': 'ɡɣ', 'classes': ["occlusives", "obstruents", "affricates"], 'types': ['voiced','backcon','velar'], 'rules': []})
consonants.append({'IPA': 'qχ', 'classes': ["occlusives", "obstruents", "affricates"], 'types': ['voiceless','backcon','uvular'], 'rules': []})
consonants.append({'IPA': 'ɢʁ', 'classes': ["occlusives", "obstruents", "affricates"], 'types': ['voiced','backcon','uvular'], 'rules': []})
consonants.append({'IPA': 'ʡʢ', 'classes': ["occlusives", "obstruents", "affricates"], 'types': ['voiceless','backcon','pharyngeal'], 'rules': []})
consonants.append({'IPA': 'ʔh', 'classes': ["occlusives", "obstruents", "affricates"], 'types': ['voiced','backcon','glottal'], 'rules': []})


""" All Fricatives"""
consonants.append({'IPA': 's', 'classes': ["sibilants", "stridents", "obstruents", "fricatives", "continuants"], 'types': ['voiceless','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 'z', 'classes': ["sibilants", "stridents", "obstruents", "fricatives", "continuants"], 'types': ['voiced','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 'ʃ', 'classes': ["sibilants", "stridents", "obstruents", "fricatives", "continuants"], 'types': ['voiceless','frontcon','postalveolar'], 'rules': []})
consonants.append({'IPA': 'ʒ', 'classes': ["sibilants", "stridents", "obstruents", "fricatives", "continuants"], 'types': ['voiced','frontcon','postalveolar'], 'rules': []})
consonants.append({'IPA': 'ʂ', 'classes': ["sibilants", "stridents", "obstruents", "fricatives", "continuants"], 'types': ['voiceless','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'ʐ', 'classes': ["sibilants", "stridents", "obstruents", "fricatives", "continuants"], 'types': ['voiced','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'ɕ', 'classes': ["sibilants", "stridents", "obstruents", "fricatives", "continuants"], 'types': ['voiceless','backcon','palatal'], 'rules': []})
consonants.append({'IPA': 'ʑ', 'classes': ["sibilants", "stridents", "obstruents", "fricatives", "continuants"], 'types': ['voiced','backcon','palatal'], 'rules': []})
consonants.append({'IPA': 'ɸ', 'classes': ["fricatives", "obstruents", "continuants"], 'types': ['voiceless','frontcon','bilabial'], 'rules': []})
consonants.append({'IPA': 'β', 'classes': ["fricatives", "obstruents", "continuants"], 'types': ['voiced','frontcon','bilabial'], 'rules': []})
consonants.append({'IPA': 'f', 'classes': ["fricatives", "continuants", "stridents"], 'types': ['voiceless','frontcon','labiodental'], 'rules': []})
consonants.append({'IPA': 'v', 'classes': ["fricatives", "continuants", "stridents"], 'types': ['voiced','frontcon','labiodental'], 'rules': []})
consonants.append({'IPA': 'θ̼', 'classes': ["fricatives", "obstruents", "continuants"], 'types': ['voiceless','frontcon','linguolabial'], 'rules': []})
consonants.append({'IPA': 'ð̼', 'classes': ["fricatives", "obstruents", "continuants"], 'types': ['voiced','frontcon','linguolabial'], 'rules': []})
consonants.append({'IPA': 'θ', 'classes': ["fricatives", "obstruents", "continuants"], 'types': ['voiceless','frontcon','dental'], 'rules': []})
consonants.append({'IPA': 'ð', 'classes': ["fricatives", "obstruents", "continuants"], 'types': ['voiced','frontcon','dental'], 'rules': []})
consonants.append({'IPA': 'θ̠', 'classes': ["fricatives", "obstruents", "continuants"], 'types': ['voiceless','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 'ð̠', 'classes': ["fricatives", "obstruents", "continuants"], 'types': ['voiced','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 'ɹ̠̊˔', 'classes': ["fricatives", "continuants"], 'types': ['voiceless','frontcon','postalveolar'], 'rules': []})
consonants.append({'IPA': 'ɹ̠˔', 'classes': ["fricatives", "continuants"], 'types': ['voiced','frontcon','postalveolar'], 'rules': []})
consonants.append({'IPA': 'ɻ˔', 'classes': ["fricatives", "continuants"], 'types': ['voiced','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'ç', 'classes': ["fricatives", "continuants"], 'types': ['voiceless','backcon','palatal'], 'rules': []})
consonants.append({'IPA': 'ʝ', 'classes': ["fricatives", "continuants"], 'types': ['voiced','backcon','palatal'], 'rules': []})
consonants.append({'IPA': 'x', 'classes': ["fricatives", "obstruents", "continuants"], 'types': ['voiceless','backcon','velar'], 'rules': []})
consonants.append({'IPA': 'ɣ', 'classes': ["fricatives", "obstruents", "continuants"], 'types': ['voiced','backcon','velar'], 'rules': []})
consonants.append({'IPA': 'χ', 'classes': ["fricatives", "obstruents", "continuants", "stridents"], 'types': ['voiceless','backcon','uvular'], 'rules': []})
consonants.append({'IPA': 'ʁ', 'classes': ["fricatives", "obstruents", "continuants", "stridents","rhotics","liquids"], 'types': ['voiced','backcon','uvular'], 'rules': []})
consonants.append({'IPA': 'ħ', 'classes': ["fricatives", "continuants", "stridents","rhotics","liquids"], 'types': ['voiceless','backcon','pharyngeal'], 'rules': []})
consonants.append({'IPA': 'ʕ', 'classes': ["fricatives", "obstruents", "continuants", "stridents","rhotics","liquids"], 'types': ['voiced','backcon','pharyngeal'], 'rules': []})
consonants.append({'IPA': 'h', 'classes': ["fricatives", "obstruents", "continuants", "stridents","rhotics","liquids"], 'types': ['voiceless','backcon','glottal'], 'rules': []})
consonants.append({'IPA': 'ɦ', 'classes': ["fricatives", "obstruents", "continuants", "stridents","rhotics","liquids"], 'types': ['voiced','backcon','glottal'], 'rules': []})
consonants.append({'IPA': 'ʍ', 'classes': ["continuants", "obstruents","semivowels"], 'types': ['voiceless','backcon','velar'], 'rules': []})
consonants.append({'IPA': 'ɧ', 'classes': ["fricatives", "obstruents", "continuants"], 'types': ['voiceless','backcon','velar'], 'rules': []})


""" All Approximants"""
consonants.append({'IPA': 'ʋ', 'classes': ["continuants", "vocoids","approximants"], 'types': ['voiced','frontcon','labiodental'], 'rules': []})
consonants.append({'IPA': 'ɹ', 'classes': ["continuants", "vocoids","approximants","rhotic","liquid"], 'types': ['voiced','frontcon','alveloar'], 'rules': []})
consonants.append({'IPA': 'ɻ', 'classes': ["continuants","vocoids","approximants","rhotic","liquid"], 'types': ['voiced','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'j', 'classes': ["continuants","vocoids","approximants","rhotic","liquid"], 'types': ['voiced','backcon','palatal'], 'rules': []})
consonants.append({'IPA': 'ɰ', 'classes': ["continuants", "vocoids","approximants","semivowels"], 'types': ['voiced','backcon','velar'], 'rules': []})
consonants.append({'IPA': 'ʔ̞', 'classes': ["continuants", "vocoids","approximants","semivowels"], 'types': ['voiced','backcon','glottal'], 'rules': []})
consonants.append({'IPA': 'w', 'classes': ["continuants", "vocoids","approximants","semivowels"], 'types': ['voiced','backcon','velar'], 'rules': []})


""" All Trills and Flap/Taps"""
consonants.append({'IPA': 'ⱱ̟', 'classes': ["vibrant", "tapflap"], 'types': ['voiceless','frontcon','bilabial'], 'rules': []})
consonants.append({'IPA': 'ⱱ', 'classes': ["vibrant", "tapflap"], 'types': ['voiceless','frontcon','labiodental'], 'rules': []})
consonants.append({'IPA': 'ɾ̼', 'classes': ["vibrant", "tapflap","rhotics", "liquids"], 'types': ['voiceless','frontcon','linguolabial'], 'rules': []})
consonants.append({'IPA': 'ɾ̥', 'classes': ["vibrant", "tapflap","rhotics", "liquids"], 'types': ['voiced','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 'ɾ', 'classes': ["vibrant", "tapflap","rhotics", "liquids"], 'types': ['voiceless','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 'ɽ̊', 'classes': ["vibrant", "tapflap","rhotics", "liquids"], 'types': ['voiced','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'ɽ', 'classes': ["vibrant", "tapflap","rhotics", "liquids"], 'types': ['voiceless','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'ɢ̆', 'classes': ["vibrant", "tapflap","rhotics", "liquids"], 'types': ['voiced','backcon','uvular'], 'rules': []})
consonants.append({'IPA': 'ʡ̆', 'classes': ["vibrant", "tapflap","rhotics", "liquids"], 'types': ['voiced','backcon','pharyngeal'], 'rules': []})
consonants.append({'IPA': 'ʙ̥', 'classes': ["vibrant", "trills", "vocoids"], 'types': ['voiceless','frontcon','bilabial'], 'rules': []})
consonants.append({'IPA': 'ʙ', 'classes': ["vibrant", "trills", "vocoids"], 'types': ['voiced','frontcon','bilabial'], 'rules': []})
consonants.append({'IPA': 'r̥', 'classes': ["vibrant", "trills", "vocoids","rhotics","liquids"], 'types': ['voiceless','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 'r', 'classes': ["vibrant", "trills", "vocoids","rhotics","liquids"], 'types': ['voiced','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 'ɽ̊r̥', 'classes': ["vibrant", "trills", "vocoids","rhotics","liquids"], 'types': ['voiceless','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'ɽr', 'classes': ["vibrant", "trills", "vocoids","rhotics","liquids"], 'types': ['voiced','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'ʀ̥', 'classes': ["vibrant", "trills", "vocoids","rhotics","liquids"], 'types': ['voiceless','backcon','uvular'], 'rules': []})
consonants.append({'IPA': 'ʀ', 'classes': ["vibrant", "trills", "vocoids","rhotics","liquids"], 'types': ['voiced','backcon','uvular'], 'rules': []})
consonants.append({'IPA': 'ʜ', 'classes': ["vibrant", "trills", "vocoids","rhotics","liquids"], 'types': ['voiceless','backcon','pharyngeal'], 'rules': []})
consonants.append({'IPA': 'ʢ', 'classes': ["vibrant", "trills", "vocoids","rhotics","liquids"], 'types': ['voiced','backcon','pharyngeal'], 'rules': []})


""" All Laterals """
consonants.append({'IPA': 'tɬ', 'classes': ["vibrant", "tapflap"], 'types': ['voiceless','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 'dɮ', 'classes': ["fricatives","laterals","continuants","vocoids"], 'types': ['voiced','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 'ʈɭ̊˔', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiceless','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'ɖɭ˔', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiced','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'cʎ̝̊', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiceless','backcon','palatal'], 'rules': []})
consonants.append({'IPA': 'ɟʎ̝', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiced','backcon','palatal'], 'rules': []})
consonants.append({'IPA': 'kʟ̝̊', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiceless','backcon','velar'], 'rules': []})
consonants.append({'IPA': 'ɡʟ̝', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiced','backcon','velar'], 'rules': []})
consonants.append({'IPA': 'ɬ', 'classes': ["fricatives","laterals","continuants","vocoids"], 'types': ['voiceless','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 'ɮ', 'classes': ["fricatives","laterals","continuants","vocoids"], 'types': ['voiced','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 'ɭ̊˔', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiceless','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'ɭ˔', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiced','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'ʎ̝̊', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiceless','backcon','palatal'], 'rules': []})
consonants.append({'IPA': 'ʎ̝', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiced','backcon','palatal'], 'rules': []})
consonants.append({'IPA': 'ʟ̝̊', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiceless','backcon','velar'], 'rules': []})
consonants.append({'IPA': 'ʟ̝', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiced','backcon','velar'], 'rules': []})
consonants.append({'IPA': 'l', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiced','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 'ɭ', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiced','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'ʎ', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiced','backcon','palatal'], 'rules': []})
consonants.append({'IPA': 'ʟ', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiced','backcon','velar'], 'rules': []})
consonants.append({'IPA': 'ʟ̠', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiced','frontcon','velar'], 'rules': []})
consonants.append({'IPA': 'ɺ̥', 'classes': ["liquids","laterals","rhodics","tapflaps"], 'types': ['voiceless','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 'ɺ', 'classes': ["liquids","laterals","rhodics","tapflaps"], 'types': ['voiced','frontcon','alveolar'], 'rules': []})
consonants.append({'IPA': 'ɭ̥̆', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiceless','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'ɭ̆', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiced','frontcon','retroflex'], 'rules': []})
consonants.append({'IPA': 'ʎ̆', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiced','backcon','palatal'], 'rules': []})
consonants.append({'IPA': 'ʟ̆', 'classes': ["affricates","laterals","continuants","vocoids"], 'types': ['voiced','backcon','uvular'], 'rules': []})

sounds = {}
sounds["vowels"] = vowels
sounds["consonants"] = consonants

file_path = 'sounds.json'
with open(file_path, 'w') as file:
    json.dump(sounds, file, indent=2)

# file_path = 'sounds.json'
# with open(file_path, 'r') as file:
#     json_data = file.read()

# data_dict = json.loads(json_data)

# print(data_dict)

