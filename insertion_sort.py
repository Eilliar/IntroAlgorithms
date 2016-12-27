def insertion_sort(A):
	"""
	Insertion sort Algorithm
	Inputs:
	- A -> list of integers
	Outputs:
	- A -> sorted list of integers
	"""
	sorted_A = []
	
	for j in range(1, len(A)):
		key = A[j]
		i = j - 1
		while (i >= 0) & (A[i] > key):
			A[i+1] = A[i]
			i = i-1
		A[i+1] = key
	return A

if __name__ == "__main__":
	teste = [5, 2, 4, 6, 1, 3]
	print insertion_sort(teste)