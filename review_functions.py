import string
import random
import re
import json


path_start = r"C:\Users\Turcanhydgoongod\Downloads\english-dict\D"
path_end = ".json"
letters = string.ascii_uppercase[:27]

with open('english_dict.json','r') as file:
    english_dict = json.loads(file.read())

def review_changer(review):
    letters = string.ascii_uppercase[:27]
    review_as_list = re.split('(\W)',review)
    test_set = {'Noun','Adjective'}
    for index, word in enumerate(review_as_list):
        if len(word) <= 1:
            continue
        capital = word[0].isupper()
        word = word.upper()
        letter = word[0]
        if (letter in letters and
                word in english_dict[letter].keys() and 
            (not {meaning[0] for meaning in english_dict[letter][word]['MEANINGS'].values()}.isdisjoint(test_set))):
            replacement = random.choice(english_dict[letter][word]['SYNONYMS'] if 
                          english_dict[letter][word]['SYNONYMS'] else 
                          word.lower())
            review_as_list[index] = replacement.capitalize() if capital else replacement.lower()
    return "".join([word for word in review_as_list])


def review_changer(review):
    letters = string.ascii_uppercase[:27]
    #review_as_list = review.split(" ")
    review_as_list = re.split('(\W)',review)
    test_set = {'Noun','Adjective'}
    for index, word in enumerate(review_as_list):
        if len(word) <= 1:
            continue
        capital = word[0].isupper()
        word = word.upper()
        letter = word[0]
        if (letter in letters and
                word in english_dict[letter].keys() and 
            (not {meaning[0] for meaning in english_dict[letter][word]['MEANINGS'].values()}.isdisjoint(test_set))):
            replacement = random.choice(english_dict[letter][word]['SYNONYMS'] if 
                          english_dict[letter][word]['SYNONYMS'] else 
                          word.lower())
            review_as_list[index] = replacement.capitalize() if capital else replacement.lower()
    return "".join([word for word in review_as_list])