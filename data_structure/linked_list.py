class Node:

	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next


class LinkedList:

	def __init__(self):
		self.first_node = None
		self.curr_node = None

	def add(self, data):
		if self.first_node == None:
			self.first_node = Node(data)
		else:
			node = self.first_node
			while node.next != None:
				node = node.next
			node.next = Node(data)
			# self.curr_node.next = Node(data)
			# self.curr_node = self.curr_node.next

	def print_list(self):
		out = "LinkedList [ "
		node = self.first_node
		while node != None:
			if node.next !=None:
				out += str(node.data) + "->"
			else:
				out += str(node.data)
			node = node.next
		out += " ]"
		print(out)

	# def __str__(self):
	# 	out = "Linked List [ "
	# 	node = self.first_node
	# 	while node.next != None:
	# 		out += str(node.data)+"->"
	# 	return out

l = LinkedList()
l.add(5)
l.add(10)
l.add(15)
l.print_list()