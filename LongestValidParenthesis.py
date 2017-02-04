class Solution(object):
	    def longestValidParentheses(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		maxLen = 0
		lastIndex = -1
		lefts = []
		
		for i in range(0, len(s)):
			if s[i] == '(':
				lefts.append(i)
			else:
				if len(lefts) == 0:
					lastIndex = i
				else:
					lefts.pop()
					if len(lefts) == 0:
						maxLen = max(maxLen, i - lastIndex)
					else:
						maxLen = max(maxLen, i - lefts[-1])
					
		return maxLen