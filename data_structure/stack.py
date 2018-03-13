class Stack:

	def __init__(self):
		self.count = 0
		self.list = []

	def push(self, data):
		self.list.append(data)
		self.count+=1
		

	def pop(self):
		output = self.list[self.count-1]
		del self.list[self.count-1]
		self.count-=1
		return output

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())