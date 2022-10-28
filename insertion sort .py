
def insertionSort(array):
	for i in range(1, len(array)):

		key = array[i]
		j = i-1
		while j >=0 and key < array[j] :
				array[j+1] = array[j]
				j -= 1
		array[j+1] = key



array = [12, 11, 13, 5, 6]
insertionSort(array)
list = [] 
print("Sorted array is : ")
for i in range(len(array)):
	list.append(array[i])	 
print(list)



