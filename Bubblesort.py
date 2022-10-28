def bubbleSort(simple):
	n = len(simple)
	ans = False
	for i in range(n-1):
		for j in range(0, n-i-1):
			if simple[j] > simple[j + 1]:
				ans = True
				simple[j], simple[j + 1] = simple[j + 1], simple[j]
		
		if not ans:
			return



simple = [9,3,5,6,2,7,45]

bubbleSort(simple)

print("Sorted array is:")
for i in range(len(simple)):
	print("% d" % simple[i], end=" ")
