## Problem 7 - 10001st prime

## By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
## What is the 10 001st prime number?

from pylab import *
n_limit=10001
n=2
k=1
al=0
while n!=n_limit:
	if al==0:
		p=6*k-1
		al=1
	else:
		p=6*k+1
		al=0
		k=k+1
		f=3
		temp=3
		r=sqrt(p)
		c=1
		while f<=r:
			if p%f==0:
				c=0
				break
			else:
				temp=temp+2
				f=f+2
			if (c==1) and (temp==f):
				n=n+1
print(n,p)

## Answer: 104743
