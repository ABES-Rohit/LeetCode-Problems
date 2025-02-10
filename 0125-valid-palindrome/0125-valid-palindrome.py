class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst=list()
        for i in s:
            if i.isalnum():
                lst.append(i.lower())
        t=''.join(lst)
        r=''.join(reversed(t))
        return (r==t)        
        