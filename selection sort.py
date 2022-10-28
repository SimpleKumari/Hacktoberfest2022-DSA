
def selectionSort(arrr, size):
	
	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):
			
			if arrr[j] < arrr[min_index]:
				min_index = j
		(arrr[ind], arrr[min_index]) = (arrr[min_index], arrr[ind])

p = [-2, 45, -7, 11, -1,88,67,202,748]
size = len(p)
selectionSort(p, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(p)
