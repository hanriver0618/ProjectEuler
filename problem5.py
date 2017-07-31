## Problem 5 - Smallest multiple
## 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
## What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

for i in range(10000000):
	a=(i+1)*19*17*13*11
	n=0
	for j in range(19):
		if a % (j+2)!=0:
			break
		else:
			n=n+1
	if n==19:
		break

print(n,a)

## Answer: 232792560
