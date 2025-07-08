class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        max_len=0
        for i in range(len(s)):
            # for odd length string
            l,r=i,i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if(r-l+1 > max_len):
                    ans=s[l:r+1]
                    max_len=r-l+1
                l=l-1
                r=r+1
            l,r=i,i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if(r-l+1 > max_len):
                    ans=s[l:r+1]
                    max_len=r-l+1
                l=l-1
                r=r+1
        return ans            

        