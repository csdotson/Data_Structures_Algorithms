'''
Problem: Given a list of words, find words that are anagrams of one another
'''
from collections import defaultdict

def find_anagrams(words):
     sorted_strings = defaultdict(list)

     for w in words:
         sorted_strings[''.join(sorted(w))].append(w)

     return [group for group in sorted_strings.values() if len(group) >= 2]

    