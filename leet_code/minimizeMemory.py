def minimize(process, n, m):
	record = {}

	while n%2==0:
		for i in range(0, n, m):
			if process[i] == process[-1]:
				break

			record[process[i]] = process[i]+process[i+1]

		del record[max(record, key=record.get)]

		return sum(record.values())
		break 

	for i in range(0, n):
		if process[i] == process[-1]:
			break

		record[process[i]] = process[i]+process[i+1]

	del record[max(record, key=record.get)]


	return sum(record.keys())

process = [10, 4, 8, 1]
n = len(process)
m = 2

print(minimize(process, n, m))