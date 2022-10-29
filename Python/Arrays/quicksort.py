def partition_of_given_array(brr, L, H):
	pivot = brr[H]

	# Pointer for greater element
	i = L - 1

	# Traverse through all elements
	for j in range(L, H):
		if brr[j] <= pivot:
			i = i + 1
			(brr[i], brr[j]) = (brr[j], brr[i])
	(brr[i + 1], brr[H]) = (brr[H], brr[i + 1])
	return i + 1


def quick_sort(brr, L, H):
	if L < H:
		w = partition_of_given_array(brr, L, H)
		quick_sort(brr, L, w - 1)
		quick_sort(brr, w + 1, H)

array = [100,700,800,300,200]
quick_sort(array, 0, len(array) - 1)

print(f'Sorted array: {array}')
