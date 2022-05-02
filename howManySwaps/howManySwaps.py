"Build an Algorithm that will count how many swaps "
"are required to sort the array."

def howManySwaps(a):
	n = len(a)
	swaps = 0

	if n < 1 or n > 10**5 or a[-1] > 10**9:
		return "Constrains does not meet the required criteria"

	while a != sorted(a):

		for i in range(0, n-1):
			if a[i] > a[i+1]:
				if a[i] < 1 or a[i] > 10**9:
					return "Constrains does not meet the required criteria"
				
				first_pair = a.pop(i)
				second_pair = a.pop(i)

				a.insert(i, second_pair)
				a.insert(i+1, first_pair)
				swaps += 1

	return swaps

a = [5, 1, 4, 2]

if __name__ == '__main__':
	print(howManySwaps(a))