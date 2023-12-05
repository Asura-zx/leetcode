'''
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated
with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
'''
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        minstring=min(str1,str2)
        maxstring=max(str1,str2)
        a=""
        for w in minstring:
            a+=w
            if (minstring.replace(a,"")=="" and maxstring.replace(a,""))=="":
                return a
            else:
                continue
                
    print(gcdOfStrings(1,'ABABABABABABABAB','ABAB'))
