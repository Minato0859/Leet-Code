# Overview
# We are given two strings word1 and word2.

# Our task is to merge the strings by adding letters in alternating order, starting with word1. If one string is longer than the other, the additional letters must be appended to the end of the merged string.

# We must return the merged string that has been formed.

class Solution:
    from itertools import zip_longest

    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = ''

        for x, y in zip_longest(word1, word2, fillvalue=''):
            #zip_longest lets one continue iterating over the longer iterable with a fill value to use in replacement of the shorter iterable
            merged_word += x + y

        return merged_word

# Input
# word1 =
# "abc"
# word2 =
# "pqr"
# Output
# "apbqcr"
# Expected
# "apbqcr"
