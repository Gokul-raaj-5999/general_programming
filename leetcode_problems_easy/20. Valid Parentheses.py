class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)//2
        
        for i in range(0,l+1):
            if '()' in s:
                s = s.replace('()', '')
            elif '[]' in s:
                s = s.replace('[]', '')
            elif '{}' in s:
                s = s.replace('{}', '')
        if(len(s) == 0):
            return(1)
        else:
            return(0)
        
