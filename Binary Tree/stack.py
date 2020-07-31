'''
   Stack initialisation for Reverse order traversals.
   Stack (Datastructure) can be related stack
   in daily life. The first element to get into the stack
   is the last element on which certain operations are performed.
'''			
class stack:
	'''Initialising the stack making it as list on which certain operations can 
		performed and modified results will be presented to the user.
	'''
	def __init__(self):
		self.items = []
	'''Checking whether the list is empty or not.'''
	def isempty(self):
		return len(self.items)==0	
	'''Insert element to list at index(0).'''
	def push(self, item):
		self.items.insert(0, item)
	'''Delete element at the top of stack.'''	
	def pop(self):
		return self.items.pop(0)
	'''Show the list version of stack.'''	
	def show(self):
		return self.items
	'''Returns the size of the list version of stack.'''	
	def size(self):
		return len(self.items)	
	'''Return the top element of the stack.'''	
	def first(self):
		return self.items[0]
	'''Return the end element of the stack.'''	
	def last(self):
		return self.items[self.size()-1]		

if __name__ == "__main__":
	Stack = stack()
	Stack.push(3)
	Stack.push(4)
	Stack.push(5)
	Stack.push(6)
	print("Size of Stack: ", Stack.size())
	print("Stack: ", Stack.show())
	Stack.pop()
	print("Size of Stack now: ", Stack.size())
	print("Top element of Stack: ", Stack.first())
	print("Bottom element of Stack: ", Stack.last())
