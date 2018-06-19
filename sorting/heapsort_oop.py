class HeapSort(object):

	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def upNode(self, index):
		while index // 2 > 0:
			if self.heapList[index] > self.heapList[index // 2]:
				self.heapList[index], self.heapList[index // 2] = self.heapList[index // 2], self.heapList[index]
			i = i // 2

	def downNode(self, index):
		while (i * 2) <= self.currentSize:
			mc = self.minChild(index)
			if self.heapList[index] > self.heapList[mc]:
				self.heapList[index], self.heapList[mc] = self.heapList[mc], self.heapList[index]:
			index = mc

	def insert(self, data):
		self.heapList.append(data)
		self.currentSize +=1
		self.upNode(currentSize)

	def minChild(self, index):
		if self.heapList[index * 2] < self.heapList[index * 2 + 1]:
		 	return index * 2 + 1
		else:
			return index * 2

	def delMin(self):
		