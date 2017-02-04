class Solution(object):
	    def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		
		has = {}
		
		for i in range(0, len(nums)):
			rest = target - nums[i]
			if rest in has:
				return [has[rest], i]
			has[nums[i]] = i
			
		return [-1, -1]