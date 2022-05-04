def remove_IDS(arr, rem):

	record = {}
	list_new = []
	count = 0

	for i in range(n):
		if arr[i] in record:
			record[arr[i]] += 1
		else:
			record[arr[i]] = 1

	for b in record:
		list_new.append([record[b], b])

	list_new.sort()

	size = len(list_new)


	for i in range(size):
		if (list_new[i][0] <= rem):
			rem -= list_new[i][0]
			count += 1
		else:
			return size - count

arr = [1, 1, 1, 2, 3, 2, 2, 2, 2, 2]
n = len(arr)
rem = 2


print(remove_IDS(arr, rem))