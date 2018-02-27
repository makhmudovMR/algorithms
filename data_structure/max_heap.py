class MaxHeap(object):

	def __init__(self, items=[]):
		# super().__init__()
		self.heap = [0]
		for i in items:
			self.heap.append(i)
			self.__floatUp(len(self.heap)-1)

	def push(self, data):
		'''Втсаляем данные в дерево, затем сортируем дерево'''
		self.heap.append(data)
		self.__floatUp(len(self.heap) - 1)

	def peek(self):
		'''Выборка максимального значения'''
		if self.heap[1]:
			return self.heap[1]
		else:
			return False

	def pop(self):
		if len(self.heap) > 2:
			self.__swap(1, len(self.heap) - 1)
			max = self.heap.pop()
			self.__bubleDown(1)
		elif len(self.heap) == 2:
			max = self.heap.pop()
		else:
			max = False
		return max

	def __swap(self, i, j):
		'''Метод замены'''
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def __floatUp(self, index):
		'''Этот метод поднимает ноду вверх в случае если она больше родителя, до тех пор пока index больше parent'''
		parent_index = int(index / 2)
		if index <=1:
			return
		elif self.heap[index] > self.heap[parent_index]:
			self.__swap(index, parent_index)
			self.__floatUp(parent_index)

	def __bubbleDown(self, index):
		left = index * 2
		right = index * 2 + 1
		largest = index
		if len(self.heap) > left and self.heap[largest] < self.heap[left]:
			largest = left
		if len(self.heap) > right and slef.heap[largest] < self.heap[right]:
			largest = right
		if largest != index:
			self.__swap(index, largest)
			self.__bubbleDown(largest)

m = MaxHeap([95,3,21])
m.push(10)
m.push(3)
m.push(1)
print(m.heap)

print(m.peek())