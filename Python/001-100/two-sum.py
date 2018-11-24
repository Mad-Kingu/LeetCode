class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dicti = {}
        result = list()
        for i in range(nums.__len__()):
            remain = target - nums[i]
            if dicti.has_key(remain):
                result.append(dicti[remain])
                result.append(i)
                return result
            dicti[nums[i]] = i

        return result
