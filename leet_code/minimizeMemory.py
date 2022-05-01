def minimizeMemory(process, n, m):

	if n >= 1 and n <= 10^3 and n%2==0 and m <= n <= 10^5:
		a = 0
		record = []
		idx = 0
		
		for i in range(0, n-1):
			record.append(sum(process[i:i+m]))
			
			if a <= sum(process[i:i+m]):
				a = sum(process[i:i+m])

				if a == max(record):
					idx = i

		for i in range(0, m):
			process.pop(idx)

		return sum(process)

	else:
		return "Be sure the constrains are according to the given condition in the problem statement :D"

process = [10, 4, 8, 1]
n = len(process)
m = 2

print(minimizeMemory(process, n, m))