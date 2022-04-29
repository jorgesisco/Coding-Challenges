# Challenge

The virtual private server on the company's Web Service cloud is used to run programs that help perform calculations on large data sets. Recently, the performance of some programs has
degraded.

Technical support has recommended that processes that consume a lot of main memory should be deleted. Unfortunately, the command-line shell that you use only lets you delete processes that form a single contiguous segment of a given fixed size. The size of a contiguous segment is the number of contiguous processes in main memory.

Find the minimum amount of main memory used by all of your processes in your instance after you delete a contiguous segment of processes.

Example:

```bash
process = [10, 4, 8, 13, 201
m = 2
```

Select a fixed contiguous segment size of m = 2. The best single contiguous segment of size 2 to delete is the segment composed of process 5, which is 20KB, and process 4, which is 13KB. This results in the minimum total main memory consumption of 10KB + 4KB + 8KB = 22KB. Return 22.

![Alt text](/leet_code/challenge_img.png "Title")

## Function Description

Complete the function minimizeMemory in the editor below.

minimizeMemory has the following parameters:
int process[n]: kilobytes occupied by each process
int m: the fixed number of contiguous applications in a
segment

Returns
int: the minimum amount of main memory taken up after
the deletion of a contiguous segment of size m.

### Constraints

• 1 ≤ m ≤ n ≤ 5\*10^5
• 1 ≤ process[i] ≤ 10^3

### Sample Case

The first line contains the integer, n, the number of elements in process[]. Each of the next n lines contains an integer, process[i). The last line contains the integer, m, the size of the
contiguous segment to delete.

Sample Input:

```bash
process[] size n = 4
process = [10, 4, 8, 1]


m = 2
```

Sample Output

```bash
9
```
