####################################################################
# Efficient implementation of a Circular Buffer (aka Ring Buffer)  #
####################################################################
# 																   #
# Note - this version is only slightly faster than the one where   #
# I implemented the data structure from scratch!		           #
# 																   #
####################################################################

import collections


class CircularBuffer:
	def __init__(self, size):
		self.size = size
		self.buffer = collections.deque(maxlen=size)

	def add(self, element):
		self.buffer.append(element)

	def __repr__(self):
		return repr(self.buffer)


# For testing purposes
if __name__ == "__main__":
	buf = CircularBuffer(100000)

	for i in range(1, 200001):
		buf.add(i)
	
	print(buf)