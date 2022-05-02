# Write a function:

# class Solution { public int solution(int[] A); }

# that, given an array A of N integers, returns the  (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

a = [1, 3, 6, 4, 1, 2]

def occurrence(a):
	a = sorted(a)
	n = len(a)
	record = []

	if max(a) < 0 :
		return 1

	else:
		for i in range(0, n):
			if a[i] != a[-1] and abs(a[i]-a[i+1]) != 1 and a[i]>=-1000000 and a[i]<=1000000:
				record.append(a[i]+1)
			elif a[i] != a[-1] and abs(a[i]-a[i+1]) == 1 and a[i]>=-1000000 and a[i]<=1000000:
				record.append(a[i]+2)
		return max(record)

if __name__ == "__main__":
	print(occurrence(a))
