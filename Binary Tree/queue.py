'''
   	Queue Class initialisation for Level order traversals
   	and Reverse order traversals.
   	Queue (DataStructure) can be related as queue
   	(when you go to buy movie ticket or something else)
   	The first person of the queue gets the service first 
   	just like that we perform majority operations on first element
   	of queue. 
'''
class queue:
	'''Initialising queue with init, which only starts a list.'''
	def __init__(self):
		self.items = []
	'''Now we add elements in the queue by appending elements to the list initialised earlier.'''	
	def enqueue(self, item):
		self.items.append(item)
	'''Now we delete the top most element in the queue by poping the first element of the list.'''	
	def dequeue(self):
		return self.items.pop(0)
	'''This returns the list in which we are storing the element of the queue.'''	
	def show(self):
		return self.items			
	'''This returns the size of the queue'''	
	def size(self):
		return len(self.items)
	'''Returns the last element of the queue'''	
	def last(self):
		return self.items[self.size()-1]
	'''Return the first element of the queue'''		
	def first(self):
		return self.items[0]	
if __name__ == "__main__":
	Queue = queue()
	Queue.enqueue(6)
	Queue.enqueue(5)
	Queue.enqueue(4)
	Queue.enqueue(3)
	print("Queue: ", Queue.show())
	Queue.dequeue()
	print("Queue Now: ", Queue.show())
	print("First element: ", Queue.first())
	print("Last element: ", Queue.last())
	print("Queue Size: ", Queue.size())