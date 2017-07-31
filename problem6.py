## Problem 6 - Sum square difference
## The sum of the squares of the first ten natural numbers is,
## 12 + 22 + ... + 102 = 385
## The square of the sum of the first ten natural numbers is,
## (1 + 2 + ... + 10)2 = 552 = 3025
## Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
## Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

from pylab import *
num=100

def sum_squares(nums):
	sum=0
	for i in range(nums):
		sum+=(i+1)**2
	return sum
def sum_squares2(nums):
	s=sum(range(nums+1))
	return s**2

print(abs(sum_squares(num)-sum_squares2(num)))

## Answer: 25164150

