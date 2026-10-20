class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index
        for i,n in enumerate(nums): #enumerate lets you loop over both: val & index
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i #update map to include latest number
        return
        