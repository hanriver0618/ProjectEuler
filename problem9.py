## Problem 9 - Special Pythagorean triplet
## A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
## a^2 + b^2 = c^2
## For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
## There exists exactly one Pythagorean triplet for which a + b + c = 1000.
## Find the product abc.

from pylab import *
 
for i in range(1000):
	for j in range(1000):
		if (i+1)+(j+1)+sqrt((i+1)**2+(j+1)**2)==1000:
			print(i+1, j+1, (i+1)*(j+1)*sqrt(((i+1)**2+(j+1)**2)))

## Answer: 31875000

