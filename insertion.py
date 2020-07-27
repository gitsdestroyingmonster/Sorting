'''	
	Here is the code for Insertion Sort,
	This is pretty naive but we can write code 
	for BinaryInsertion Sorting but as the actual time complexity
 	of this code is O(n**2), So there is no point of writing 
 	this program.Here in below code L can be List,Array.
 '''
def insertionsort(L):
	n = len(L)
	# We are swap the right element with left element if it is smaller then the left element.
	for i in range(1,n):
		counter = 0
		# We swap the ith element until it becomes larger than the left element.
		for j in range(i,0,-1):
			if L[j]<L[j-1]:
				counter += 1
				print(f"Swapped {L[j]} with {L[j-1]}")
				L[j],L[j-1] = L[j-1],L[j]
		# Counter here tells us how many times the inner swaps happens for each value of j.s		
		print(counter)		
	return L
print(insertionsort([5,4,3,2,1,-1,-2,-3]))	
			