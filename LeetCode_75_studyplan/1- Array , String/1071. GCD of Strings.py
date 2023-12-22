# Overview
# In this problem, we are looking for the Greatest Common Divisor of two strings, which for convenience we will consider as the GCD string. To remove ambiguity, here we regard:

# all strings that divides both str1 and str2 as divisible strings.
# the longest string among all divisible strings as the GCD string.


# simple sol:
## from math import gcd
# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         if str1+str2 != str2+str1:
#             return ""
#         max_length = gcd(len(str1), len(str2))
#         return str1[:max_length]


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if len(str1) > len(str2):
            shortstr = str2
            bigstr = str1
        else:
            shortstr = str1
            bigstr = str2
        
        divides = False
        gcdstr = shortstr
        i = 1

        while not divides:
            
            if (len(bigstr) % len(gcdstr) == 0) and (len(shortstr) % len(gcdstr) == 0):
               divides = True
            else:
                gcdstr = shortstr[:-i]   
                i += 1

        loops = len(bigstr) / len(gcdstr)
        start = 0
        end = len(gcdstr)

        while end <= len(bigstr):
            
            if gcdstr != bigstr[start:end]:
                return ''
            else:
                start += len(gcdstr)
                end += len(gcdstr)   
        
        start = 0
        end = len(gcdstr)


        while end <= len(shortstr):
            
            if gcdstr != shortstr[start:end]:
                return ''
            else:
                start += len(gcdstr)
                end += len(gcdstr)   

        return gcdstr
    