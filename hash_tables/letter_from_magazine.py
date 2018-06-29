'''
Problem 12.2: Given a text from a letter and text from a magazine, is it possible to recreate the letter from the magazine text 
'''
import collections

def letter_from_magazine(letter, magazine):
    letter_chars = collections.Counter(letter)
    mag_chars = collections.Counter(magazine)

    for char, freq in letter_chars.items():
        if mag_chars[char] >= freq:
            continue
        else:
            return False
    return True

