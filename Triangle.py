class Solution(object):
	def minimumTotal(self, triangle):
		if triangle == None:
			return 0
		if len(triangle) == 1:
			return triangle[0][0]
			
		for i in range(1, len(triangle)):
			k = len(triangle) - i - 1
			for j in range(0, len(triangle[k])):
				if triangle[k][j] + triangle[k+1][j] > triangle[k][j] + triangle[k+1][j+1]:
					triangle[k][j] = triangle[k][j] + triangle[k+1][j+1]
				else:
					triangle[k][j] = triangle[k][j] + triangle[k+1][j]
		return triangle[0][0]


solu = Solution()
print( solu.minimumTotal([[2], [3,4], [6,5,7], [4,1,8,3]]) )
print( solu.minimumTotal([[2], [3,4]]) )
print( solu.minimumTotal([[2]]) )
print( solu.minimumTotal([]) )