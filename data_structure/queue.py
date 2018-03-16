class Queue(object):

	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		if self.items != []:
			tmp = self.items[0]
			del self.items[0]
			return tmp
		else:
			return None

	def isEmpty(self):
		return self.items == []


q = Queue()
q.enqueue(1)
q.enqueue(2)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.items)
