class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = 0
        nums_index = {}
        
        for i in nums:
            if i not in nums_index:
                nums_index[i] = index
            
            index += 1
            
        index = 0 
        for i in nums:
            
            remainder = target - i    
             
            if remainder in nums_index:
                if index != nums_index[remainder]:
                    return [index, nums_index[remainder]]

            index += 1                