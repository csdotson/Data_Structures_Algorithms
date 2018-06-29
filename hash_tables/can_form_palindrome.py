'''
Problem 12.1: Given a string, test whether it's possible for the letters forming that string to be a palindrome
'''
import collections

def can_form_palindrome(str):
    return sum(v % 2 for v in collections.Counter(str).values()) <= 1