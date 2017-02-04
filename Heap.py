#!/usr/bin/python

class Heap(object):
	def build(self, elements, typ):
		i = len(elements)/2 - 1
		while i >= 0:
			self.heapify(elements, i, typ)
			i -= 1
			
	def heapify(self, elements, index, typ):
		mIndex = self.getMIndex(elements, index, typ)
		
		if mIndex != index:
			temp = elements[index]
			elements[index] = elements[mIndex]
			elements[mIndex] = temp
			self.heapify(elements, mIndex, typ)
			
	def getMIndex(self, elements, index, typ):
		leftIndex = 2*index + 1
		rightIndex = 2*index + 2
		length = len(elements)
		
		erIndex = 0
		mIndex = 0
		if rightIndex < length and leftIndex < length:
			if self.compareOps(elements[rightIndex], elements[index], typ):
				erIndex = rightIndex
			else:
				erIndex = index
			if self.compareOps(elements[leftIndex], elements[erIndex], typ):
				mIndex = leftIndex
			else:
				mIndex = erIndex
		elif leftIndex < length and rightIndex >= length:
			if self.compareOps(elements[leftIndex], elements[index], typ):
				mIndex = leftIndex
			else:
				mIndex = index
		else:
			mIndex = index
		
		return mIndex
	
	def compareOps(self, op1, op2, typ):
		if typ == 0:
			return op1 < op2
		else:
			return op1 > op2

	def removeTop(self, elements, typ):
		maxVal = elements[0]
		elements[0] = elements[len(elements)-1]
		elements.pop()
		self.heapify(elements, 0, typ)
		
		
# MinHeap
minHeap = Heap()
elements = [10,9,8,7,6,5,4,3,2,1]
minHeap.build(elements, 0)
print(elements)
for i in range(9):
	minHeap.removeTop(elements, 0)
	print(elements)
	
# MaxHeap
maxHeap = Heap()
elements = [1,2,3,4,5,6,7,8,9,10]
maxHeap.build(elements, 1)
print(elements)
for i in range(9):
	maxHeap.removeTop(elements, 1)
	print(elements)