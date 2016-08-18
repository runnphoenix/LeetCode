#!/usr/bin/python

class MaxHeap(object):
	def build(self, elements):
		i = len(elements)/2 - 1
		while i >= 0:
			self.heapify(elements, i)
			i -= 1
			

	def heapify(self, elements, t):
		index = t
		leftIndex = 2*t + 1
		rightIndex = 2*t + 2
		length = len(elements)
		
		biggerIndex = 0
		maxIndex = 0
		if rightIndex < length and leftIndex < length:
			if elements[index] < elements[rightIndex]:
				biggerIndex = rightIndex
			else:
				biggerIndex = index
			if elements[leftIndex] > elements[biggerIndex]:
				maxIndex = leftIndex
			else:
				maxIndex = biggerIndex
		elif leftIndex < length and rightIndex >= length:
			if elements[leftIndex] > elements[index]:
				maxIndex = leftIndex
			else:
				maxIndex = index
		else:
			maxIndex = index
		
		if maxIndex != index:
			temp = elements[index]
			elements[index] = elements[maxIndex]
			elements[maxIndex] = temp
			self.heapify(elements, maxIndex)
		

	def removeMax(self, elements):
		maxVal = elements[0]
		elements[0] = elements[len(elements)-1]
		elements.pop()
		self.heapify(elements, 0)
	
maxHeap = MaxHeap()
elements = [1,2,3,4,5,6,7,8,9,10]
maxHeap.build(elements)
print(elements)