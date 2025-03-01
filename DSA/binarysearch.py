def binarySearch(array, x, low, high):

	while low <= high:
		mid = low + (high - low)//2
		if array[mid] == x:
			return mid
		elif array[mid] < x:
			low = mid + 1
		else:
			high = mid - 1
	return -1


array = [2, 4, 5, 7, 14, 17, 19, 22]
x = 22

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
	print(str(result))
else:
	print("Not found")


	
