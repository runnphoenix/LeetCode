#!/usr/bin/python

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def isSameTree(self, p, q):
		pVals = self.trValueArray(p)
		qVals = self.trValueArray(q)
	
		if pVals == [] and qVals == []:
			return True
		elif pVals == [] and qVals != []:
			return False
		elif pVals != [] and qVals == []:
			return False
		
		if len(pVals) != len(qVals):
			return False
		for i in range(len(pVals)):
			if pVals[i] != qVals[i]:
				return False
	
		return True
		
	def trValueArray(self, p):
		if p == [] or p == None:
			return []
		
		nodes = [p]
		vals = [p.val]
			
		while len(nodes) > 0:
			firstNode = nodes[0]
			
			if firstNode.left != None and firstNode.right != None:
				nodes.append(firstNode.left)
				vals.append(firstNode.left.val)
				nodes.append(firstNode.right)
				vals.append(firstNode.right.val)
			elif firstNode.left != None and firstNode.right == None:
				nodes.append(firstNode.left)
				vals.append(firstNode.left.val)
				vals.append(None)
			elif firstNode.left == None and firstNode.right != None:
				vals.append(None)
				nodes.append(firstNode.right)
				vals.append(firstNode.right.val)
					
			nodes.remove(firstNode)
				
		return vals

		
solu = Solution()

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.left.right = TreeNode(5)
p.right.left = TreeNode(6)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)
q.left.right = TreeNode(5)
q.right.left = TreeNode(6)

print(solu.isSameTree([],[]))