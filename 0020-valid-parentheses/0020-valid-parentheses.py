class Solution:
    def isValid(self, s: str) -> bool:
        stak=[]
        combo={")":"(","}":"{","]":"["}
        for i in s:
            if i in combo.values():
                stak.append(i)
            elif(i in combo.keys()):
                if len(stak)==0 or combo[i]!=stak[-1]:
                    return False
                stak.pop()        
        return not stak            

        
        