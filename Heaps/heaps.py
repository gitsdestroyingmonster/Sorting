'''Takes an array where there is a single point of violation of max heap property then it makes that array a max heap. '''
def max_heapify(arr, n, i): 
	largest = i  #Thinking parent to be the largest
	l = 2 * i + 1	 #Left child of i
	r = 2 * i + 2	 #Right child of i 

	if l < n and arr[i] < arr[l]: #if the left child exist in array and is greater than parent i then make it the largest
		largest = l 

	if r < n and arr[largest] < arr[r]: #if the right child exist in array and is greater than parent i then make it the largest
		largest = r 

	if largest != i: # Finally if the parent is not the largest then swap parent with the larget child
		arr[i],arr[largest] = arr[largest],arr[i] 
 
		max_heapify(arr, n, largest) # Repeat this process on the largest child as now there is a chance that the max heap property gets violated


def heap_sort(arr): 
	n = len(arr) 
	# Here we are building maxheaps from leaves up to the root level of heap
	# Leaves are already considered max heaps as we have nothing to compare with them
	for i in range(n//2 - 1, -1, -1): 
		max_heapify(arr, n, i) 

	'''	
		Here we swap the root element of the heap with last element,
		discard the last element and we maintain our max heap property of heap
		as when we swap them violation of property comes only in root.
	'''	
	for i in range(n-1, 0, -1): 
		arr[i], arr[0] = arr[0], arr[i] 
		max_heapify(arr, i, 0) 
#Driver code to check that everything is working fine
if __name__ == "__main__":
	arr = [13, 6, 7, 21, 45, 9, 2, 100] 
	heap_sort(arr) 
	print(arr)
 

