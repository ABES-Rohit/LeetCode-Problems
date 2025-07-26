class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        d="".join(s).split()
        return len(d[-1])