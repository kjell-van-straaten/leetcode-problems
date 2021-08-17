class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000                 
        }
        outcome = 0
        index = 1
        for l in s:
            negate = False
            
            for j in s[index:]:
                if values[j] > values[l]:
                    negate = True
               
            if negate:
                outcome -= values[l]
            else:
                outcome += values[l]
            index += 1
        
        return outcome
            