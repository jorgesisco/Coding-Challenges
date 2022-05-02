import numpy as np

def minimumGroups(awards, k):
	awards = sorted(awards)
	n = len(awards)

	if n==0:
		return 0

	count = 1
	start = 0

	for i in range(0, n):
		if awards[i] - start > k:
			count+=1
			start = awards[i]

	return count



awards = [1, 5, 9, 6, 4, 2]
k = 3



if __name__ == "__main__":
	print(minimumGroups(awards, k))