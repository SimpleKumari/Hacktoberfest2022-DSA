def insertion_Sort(arr):
    for i in range(1, len(arr)):
        ans = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > ans: 
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = ans    
    return arr     
			
def bucket_Sort(brr):
	P = []
	s = 10 
	for i in range(s):
		P.append([])
	for j in brr:
		G = int(s * j)
		P[G].append(j)
	for i in range(s):
		P[i] = insertion_Sort(P[i])
	count= 0
	for i in range(s):
		for j in range(len(P[i])):
			brr[count] = P[i][j]
			count += 1
	return brr


x = [0.83234, 0.565, 0.666666,0.3333, 0.444, 0.3439]
print("Sorted Array : ")
print(bucket_Sort(x))

