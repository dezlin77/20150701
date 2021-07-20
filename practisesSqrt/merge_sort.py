testlist = [1,24,3,5,6,8,11,13,16,19]

def merge(left, right):
	result = []
	i , j = 0 , 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	while (i < len(left)):
		result.append(left[i])
		i += 1
	while (j < len(right)):
		result.append(right[j])
		j += 1
	print ("merge: " + str(left) + " &" + str(right))
	return result

def merge_sort(L):
	print("merge sort: " + str(L))
	if len(L) < 2:
		return L[:]
	else:
		middle = len(L)//2
		left = merge_sort(L[:middle])
		right = merge_sort(L[middle:])
		return merge(left, right)

print ("")
print (merge_sort(testlist))
