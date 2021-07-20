testlist = [1,24,3,5,6,8,11,13,16,19]

def bubble_sort(l):
	swap = False
	while not swap:
		print ("bubble sort: " + str(l))
		swap = True
		for j in range (1, len(l)):
			if l[j-1] > l[j]:
				swap = False
				temp = l[j]
				l[j] = l[j-1]
				l[j-1] = temp

print ("")
print (bubble_sort(testlist))
print (testlist)
