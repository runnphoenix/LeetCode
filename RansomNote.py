#!/usr/bin/python

class Solution(object):
	def canConstruct(self, ransomNote, magazine):
		magaArray = []
		for cha in magazine:
			magaArray.append(cha)
		for cha in ransomNote:
			if cha not in magaArray:
				return False
			else:
				magaArray.remove(cha)
		return True
		
solu = Solution()
print(solu.canConstruct("aabb", "ab"))
