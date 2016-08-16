#!/usr/bin/python

# Definition for a binary tree node.

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def invertTree(self, root):
		if root == None:
			return None
					
		if root.left == None and root.right == None:
			return root
		else:
			temp = root.right
			root.right = root.left
			root.left = temp
					
			self.invertTree(root.left)
			self.invertTree(root.right)
					
			return root
			
class PrintTree(object):
	# 宽度优先
	def prTree(self, root):
		if root == None:
			return None
			
		nodes = [root]
		vals = [root.val]
		
		while len(nodes) > 0:
			current = nodes[0]
			if current.left != None or current.right != None:
				if current.left != None:
					nodes.append(current.left)
					vals.append(current.left.val)
				if current.right != None:
					nodes.append(current.right)
					vals.append(current.right.val)
			nodes.remove(current)
		print(vals)

#################################################################	
# 建树
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
# 打印树
pr = PrintTree()
pr.prTree(root)
# 反转树并打印
solution = Solution()
solution.invertTree(root)
pr.prTree(root)