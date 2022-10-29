def count_Sort(P):

	
	solution = [0 for j in range(len(P))]

	
	count = [0 for j in range(256)]

	
	ans = ["" for _ in P]


	for j in P:
		count[ord(j)] += 1

	
	for j in range(256):
		count[j] += count[j-1]

	
	for j in range(len(P)):
		solution[count[ord(P[j])]-1] = P[j]
		count[ord(P[j])] -= 1

	
	for j in range(len(P)):
		ans[j] = solution[j]
	return ans

array = "SimpleAnushkaHimanshuAnkurPrernaSamarth"
ans = count_Sort(array)
print("Sorted character array is % s" %("".join(ans)))

