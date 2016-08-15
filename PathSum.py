#!/usr/bin/python

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
		if root == None:
			return False
		
		if root.left != None and root.right != None:
			self.hasPathSum(root.left, sum - root.val)
			self.hasPathSum(root.right, sum - root.val)
		elif root.left == None and root.right != None:
			self.hasPathSum(root.right, sum - root.val)
		elif root.left != None and root.right == None:
			self.hasPathSum(root.left, sum - root.val)
		else:
			if sum == root.val:
				return True
			else:
				return False
			
solu = Solution()

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

print(solu.hasPathSum(root, 22))