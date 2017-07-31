## Problem 10 - Summation of primes 
## The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
## Find the sum of all the primes below two million.

from pylab import *
sum=5 ## 2 and 3
p=5
limit=2000000
k=1
a=0
while p<=limit:
        c=0
        if a==0:
                p=6*k-1
                a=1
        else:   
                p=6*k+1
                a=0
                k=k+1
        if p>limit:
                break
        f=3     
        r=sqrt(p)
        while f <= r:
                if p % f ==0:
                        c=1
                        break
                f=f+2   
        if c==0:
                sum=sum+p
print(sum)    

-->142913828922
