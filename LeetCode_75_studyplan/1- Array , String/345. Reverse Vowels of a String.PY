# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "hello"
# Output: "holle"

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"
 

# Constraints:
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels_in_word = []

        list_s = list(s)

        for char in s:
            if char in vowels:
                vowels_in_word.append(char)
        
        vowels_in_word.reverse()

        for i in range(len(s)):
            if s[i] in vowels:
                list_s[i] = vowels_in_word[0]
                del vowels_in_word[0]
        
        return ''.join(list_s)
    
    
    
    # 27 ms Sol:
    # class Solution:
    #     def reverseVowels(self, s: str) -> str:
    #         vowelsSet = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'}
    #         stack = [v for v in s if v in vowelsSet]
    #         strResult = ""
    #         for c in s:
    #             strResult += stack.pop() if c in vowelsSet else c
    #         return strResult
    
    # 50 ms Sol:
    # class Solution:
        #  def reverseVowels(self, s: str) -> str:
        #     vowelsSet = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'}
        #     stack = [v for v in s if v in vowelsSet]
        #     strResult = ""
        #     for c in s:
        #         strResult += stack.pop() if c in vowelsSet else c
        #     return strResult


        
        