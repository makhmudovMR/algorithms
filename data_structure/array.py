class Array(object):

	array = None

	def __init__(self, count_cells):
		self.array = [None for x in range(count_cells)]

	def put(self, index, data):
		self.array[index] = data

	def delete(self, index):
		del self.array[index]
		#self.array.remove(index)

	def __str__(self):
		arr_str = "[ "
		for i in self.array:
			arr_str += str(i) + " "
		arr_str += "]"
		return arr_str


a = Array(4)
print(a)
a.put(0,"hello world")
print(a)
a.delete(3)
print(a)
a.put(1,23)
print(a)