####################################################################
# Elaborate implementation of a Circular Buffer (aka Ring Buffer)  #
####################################################################
# For the purpose of implementing the whole algorithm on one's own #
# 																   #
# Note - this version is only slightly slower than the one which   #
# uses the built-in data structure deque from collections. The     #
# bottleneck is the __repr__ function (in both implementations).   #
####################################################################

class Node:
	def __init__(self, value):
		self.value = value
		self.next_node = None

	def set_next(self, new_node):
		self.next_node = new_node

	def get_next(self):
		return self.next_node

	def get_value(self):
		return self.value


class CircularBuffer:
	def __init__(self, max_size):
		self.size = 0
		self.max_size = max_size
		self.head_node = None
		self.tail_node = None

	def add(self, value):
		new_node = Node(value)

		if self.head_node == None:
			self.head_node = new_node
			self.tail_node = new_node
			self.size += 1

		else:
			if self.size < self.max_size:
				self.tail_node.set_next(new_node)
				self.tail_node = new_node
				self.size += 1

			else:
				self.head_node = self.head_node.get_next()
				self.tail_node.set_next(new_node)
				self.tail_node = new_node

	def __repr__(self):
		current_node = self.head_node
		lst = []

		while current_node:
			lst.append(current_node.get_value())
			current_node = current_node.get_next()

		return f"{lst} - size: {self.size} - max_size: {self.max_size}"


# For testing purposes
if __name__ == "__main__":
	buf = CircularBuffer(100000)

	for i in range(1, 200001):
		buf.add(i)

	print(buf)
