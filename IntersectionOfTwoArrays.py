#!/usr/bin/python

class Solution(object):
	def intersection(self, nums1, nums2):
		nums1Set = set(nums1)
		nums2Set = set(nums2)
		result = []
		
		for num in nums1Set:
			if num in nums2Set:
				result.append(num)
		
		return result
		
solution = Solution()
xx = solution.intersection([2,3,4], [4])
print(xx)