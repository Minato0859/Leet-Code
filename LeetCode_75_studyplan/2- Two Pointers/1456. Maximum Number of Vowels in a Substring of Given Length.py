# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
       
        vowels = 'aeiou'
        substring = s[:k]
        count = max_count = sum([1 for char in substring if char in vowels])




        for i in range(k,len(s)):

            if s[i-k] in vowels:
                count -= 1
            if s[i] in vowels:
                count +=1
            
            max_count = max(count, max_count)


        return max_count               