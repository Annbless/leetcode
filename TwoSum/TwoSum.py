class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)):
            try:
                temp = nums[x]
                pos = nums[x+1:len(nums)+1].index(target - temp)
            except:
                pass
            else:
                break
        return [x,pos + x + 1]