# Python3 program for implementation 
# of Heap Sort 

# To heapify a subtree rooted with 
# node i which is an index in arr[]. 
# n is size of heap 
def heapify(arr, sizeofheap, i): 
	smallest = i # Initialize smalles as root 
	left_child = 2 * i + 1 # left = 2*i + 1 
	right_child = 2 * i + 2 # right = 2*i + 2 

	# If left child is smaller than root 
	if left_child < sizeofheap and arr[left_child] < arr[smallest]: 
		smallest = left_child 

	# If right child is smaller than 
	# smallest so far 
	if right_child < sizeofheap and arr[right_child] < arr[smallest]: 
		smallest = right_child 

	# If smallest is not root 
	if smallest != i: 
		(arr[i], arr[smallest]) = (arr[smallest],arr[i]) 

		# Recursively heapify the affected 
		# sub-tree 
		heapify(arr, sizeofheap, smallest) 

# main function to do heap sort 
def heapSort(arr, sizeofheap): 
	
	# Build heap (rearrange array) 
	for i in range(int(sizeofheap / 2) - 1, -1, -1): 
		heapify(arr, sizeofheap, i) 

	# One by one extract an element 
	# from heap 
	for i in range(sizeofheap-1, -1, -1): 
		
		# Move current root to end # 
		arr[0], arr[i] = arr[i], arr[0] 

		# call max heapify on the reduced heap 
		heapify(arr, i, 0) 

# A utility function to print 
# array of size n 
def printArray(arr, n):	
	for i in range(n): 
		print(arr[i], end = " ") 
	print() 

# Driver Code 
if __name__ == '__main__': 
	arr = [1, 4, 6, -6, 9, 3, 0, 8] 
	n = len(arr)
	print("Initial Array is : ")
	printArray(arr,n)
	heapSort(arr, n)
	print("SORTED ARRAY is : ") 
	printArray(arr, n) 
