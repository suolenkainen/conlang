# conlang
Functions to modify sound changes in conlangs

## Sounds
Includes most IPA sounds.

Syntax: {'IPA': 'i', "classes": [], 'types': [], 'forbidden': []}

CLASSES
- vowels (Vowel)
- nasals (Consonant)
- plosives (Consonant)
- sibilants (Consonant)
- fricatives (Consonant)
- continuants (Consonant)
- vibrant (Consonant)
- affricates (Consonant)
- liquids (Consonant)
- stridents (Consonant)
- occlusives (Consonant)
- vocoids (Consonant)
- rhotic (Consonant)
- semivowels (Consonant)
- obstruents (Consonant)
- rhotics (Consonant)
- liquid (Consonant)
- tapflaps (Consonant)
- rhodics (Consonant)
- approximants (Consonant)
- tapflap (Consonant)
- laterals (Consonant)
- trills (Consonant)

TYPES
- front (Vowel)
- high (Vowel)
- rounded (Vowel)
- retracted (Vowel)
- raised (Vowel)
- forbidden (Vowel)
- low (Vowel)
- unrounded (Vowel)
- voiceless (Consonant)
- voiced (Consonant)
- frontcon (Consonant)
- backcon (Consonant)
- bilabial (Consonant)
- labiodental (Consonant)
- linguodental (Consonant)
- alveloar (Consonant)
- retroflex (Consonant)
- palatal (Consonant)
- velar (Consonant)
- uvular (Consonant)
- postalveolar (Consonant)
- glottal (Consonant)
- alveolar (Consonant)
- linguolabial (Consonant)
- pharyngeal (Consonant)
- dental (Consonant)

- forbidden - Rules where the sound is forbidden (TBD)

## Stresses

### Different rules of placing stress

1. Only the vowel sound within a syllable is stressed; stress is not applied to consonant sounds.
2. Any given word, even one with many syllables, will only have one syllable that receives the primary stress in speech. 

By definition, single-syllable words only ever have a single stress.
Some longer words also receive a secondary stress (TBD)

### Determining stress based on word type
Nouns, adjectives, verbs, prepositions, etc. might have different rules

Since some words are pronunciated the same even though they mean different word classes,
placing stress on other syllable helps distinguish them

Compound words can have different stresses. Words with prefixes and suffixes can create different
stress rules. 

There are also unstressed words that usually are one syllable words. These are usually 
lexical words like pronouns, prepositions, conjunctions, articles, determiners, and auxiliary verbs.

Length of the syllable can also affect the placement of the stress

## Syntaxes
The following stntaxes are used in this program:
- Sounds: {'IPA': '', 'classes': [], 'types': [], 'forbidden': []}
- Syllables: {'sounds': [{'IPA': ''...},...], 'stressed': True}
- Words: {'syllables': [{'sounds': [{'IPA': ''...},...], 'stressed': True}, ..., TBD]}