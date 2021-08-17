class Solution:
    def longestCommonPrefix(self, strs) -> str:
        count=0
        for i in range(len(strs[0])):
            prefix = strs[0][:len(strs[0])-i]
            
            all_good = True
            for j in strs:
                print(j)
                print(prefix)
                if prefix == j[:len(prefix)]:
                    
                    continue
                else:
                    all_good = False
                    break
            
            if all_good:
                count += 1
            
        if count == 0:
            return ""
        else:
            return strs[0][:count-1]


test = Solution()
test.longestCommonPrefix(["c","acc","ccc"])