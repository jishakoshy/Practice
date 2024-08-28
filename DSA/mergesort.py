def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]        # Dividing the array elements into 2 halves
        R = arr[mid:]

        merge_sort(L)        # Sorting the first half
        merge_sort(R)        # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Example usage
arr = [12, 3, 5, 6, 14]
merge_sort(arr)
print("Sorted array is:", arr)






# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]

# Eg:-
# arr = [11,12,22,90,43,34,21]
# m = l+(r-l)//2,  m => 3
# n = 7,
#  n1 = 4, n2 = 3

# def merge(arr, l, m, r):
# 	n1 = m - l + 1
# 	n2 = r - m

# 	# create temp arrays
# 	L = [0] * (n1)
# 	R = [0] * (n2)

# 	# Copy data to temp arrays L[] and R[]
# 	for i in range(0, n1):
# 		L[i] = arr[l + i]

# 	for j in range(0, n2):
# 		R[j] = arr[m + 1 + j]

# 	# Merge the temp arrays back into arr[l..r]
# 	i = 0	 # Initial index of first subarray
# 	j = 0	 # Initial index of second subarray
# 	k = l	 # Initial index of merged subarray

# 	while i < n1 and j < n2:
# 		if L[i] <= R[j]:
# 			arr[k] = L[i]
# 			i += 1
# 		else:
# 			arr[k] = R[j]
# 			j += 1
# 		k += 1

# 	# Copy the remaining elements of L[], if there
# 	# are any
# 	while i < n1:
# 		arr[k] = L[i]
# 		i += 1
# 		k += 1

# 	# Copy the remaining elements of R[], if there
# 	# are any
# 	while j < n2:
# 		arr[k] = R[j]
# 		j += 1
# 		k += 1

# # l is for left index and r is right index of the
# # sub-array of arr to be sorted

# # l,r,m -> are index

# def mergeSort(arr, l, r):
# 	if l < r:

# 		# Same as (l+r)//2, but avoids overflow for
# 		# large l and h
# 		m = l+(r-l)//2

# 		# Sort first and second halves
# 		mergeSort(arr, l, m)
# 		mergeSort(arr, m+1, r)
# 		merge(arr, l, m, r)


# # Driver code to test above
# arr = [12,42,4,5,2,76,43,6,8,10,9,7,101,26,18,1,0,16,78,100,50,51,53]
# n = len(arr)
# print("Given array is")
# for i in range(n):
# 	print("%d" % arr[i],end=" ")

# mergeSort(arr, 0, n-1)
# print("\n\nSorted array is")
# for i in range(n):
# 	print("%d" % arr[i],end=" ")


# explanation of full code in detail go through this!!!!!!


# Let's walk through the code and explain how it works with the given array [12, 11, 13, 5, 6, 7]. We'll cover each step from the input array to the sorted array:

# Initial State:
# Original array: [12, 11, 13, 5, 6, 7]

# Call mergeSort(arr, 0, n-1) to start the sorting process.
# mergeSort Function Call:
# mergeSort(arr, 0, 5)
# This call initiates the merge sort process for the entire array.

# First Recursive Call:
# mergeSort(arr, 0, 2)
# This call sorts the left half of the array [12, 11, 13].
# Second Recursive Call:
# mergeSort(arr, 0, 1)
# This call sorts the left half of the left subarray [12, 11].
# Third Recursive Call:
# mergeSort(arr, 0, 0)
# This call sorts the single-element subarray [12].
# Since there's only one element, no further recursion occurs.
# Backtrack to Sort Right Subarray:
# After sorting the left subarray [12], the algorithm backtracks to sort the right subarray [11].
# Merge Left and Right Subarrays:
# The sorted left subarray [12] and right subarray [11] are merged into [11, 12].
# Backtrack to Sort Larger Subarray:
# After sorting and merging the left and right subarrays, the algorithm backtracks to sort the larger subarray [13].
# Fourth Recursive Call:
# mergeSort(arr, 2, 2)
# This call sorts the single-element subarray [13].
# Since there's only one element, no further recursion occurs.
# Merge Left and Right Subarrays:
# The sorted left subarray [13] and right subarray [11, 12] are merged into [11, 12, 13].
# Backtrack to Sort Larger Subarray:
# After sorting and merging the left and right subarrays, the algorithm backtracks to sort the larger subarray [5, 6, 7].
# Fifth Recursive Call:
# mergeSort(arr, 3, 5)
# This call sorts the right half of the original array [5, 6, 7].
# Sixth Recursive Call:
# mergeSort(arr, 3, 4)
# This call sorts the left half of the right subarray [5, 6, 7].
# Seventh Recursive Call:
# mergeSort(arr, 3, 3)
# This call sorts the single-element subarray [5].
# Since there's only one element, no further recursion occurs.
# Backtrack to Sort Right Subarray:
# After sorting the left subarray [5], the algorithm backtracks to sort the right subarray [6].
# Merge Left and Right Subarrays:
# The sorted left subarray [5] and right subarray [6] are merged into [5, 6].
# Backtrack to Sort Larger Subarray:
# After sorting and merging the left and right subarrays, the algorithm backtracks to sort the larger subarray [7].
# Eighth Recursive Call:
# mergeSort(arr, 5, 5)
# This call sorts the single-element subarray [7].
# Since there's only one element, no further recursion occurs.
# Merge Left and Right Subarrays:
# The sorted left subarray [7] and right subarray [5, 6] are merged into [5, 6, 7].
# Merge Final Subarrays:
# The sorted left subarray [11, 12, 13] and right subarray [5, 6, 7] are merged into the final sorted array [5, 6, 7, 11, 12, 13].
# This completes the merge sort algorithm, and the sorted array is [5, 6, 7, 11, 12, 13].




# eg for large array how it works:

#                            [12,42,4,5,2,76,43,6,8,10,9,7,101,26,18,1,0,16,78,100,50,51,53]

#             [12,42,4,5,2,76,43,6,8,10,9,7,101,26,18]                         [1,0,16,78,100,50,51,53]

#     [12,42,4,5,2,76,43]               [6,8,10,9,7,101,26,18]             [1,0,16,78,100]             [50,51,53]

# [12,42,4,5]  [2,76,43]          [6,8,10,9]       [7,101,26,18]       [1,0,16]   [78,100]           [50,51]    [53]

# [12,42] [4,5]   [2,76]  [43]    [6,8]  [10,9]   [7,101]   [26,18]     [1,0] [16] [78]  [100]       [50]  [51]    [53]

#  [12] [42] [4] [5] [2] [76] [43] [6] [8] [10] [9] [7] [101] [26] [18] [1] [0] [16] [78] [100] [50] [51] [53]



