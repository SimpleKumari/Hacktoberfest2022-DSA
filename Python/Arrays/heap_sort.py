def Heap_algorithm(p, N, L):
	ans = L 
	l = 2 * L + 1	 
	r = 2 * L + 2	 


	if l < N and p[ans] < p[l]:
		ans = l

	if r < N and p[ans] < p[r]:
		ans = r

	if ans != L:
		p[L], p[ans] = p[ans], p[L] 

		
		Heap_algorithm(p, N, ans)


def heapSort(p):
	N = len(p)

	
	for i in range(N//2 - 1, -1, -1):
		Heap_algorithm(p, N, i)

	for i in range(N-1, 0, -1):
		p[i], p[0] = p[0], p[i] 
		Heap_algorithm(p, i, 0)

if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]

	
	heapSort(arr)
	N = len(arr)

	print("Sorted array :")
	for i in range(N):
		print("%d" % arr[i], end=" ")

