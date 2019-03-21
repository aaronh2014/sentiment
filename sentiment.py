import re

def remove_rating(sentence):
    patterns = ['\[\d*\]', '\(\d*\)', '\{\d*\]', '\[\d*\}']
    for p in patterns:
        sentence = re.sub(p,'',sentence)
    return sentence

def extract_rating(sentence):
    return re.search('\[\d*\]',sentence)


    
    
