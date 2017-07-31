## Problem 23 - Non-abundant sums
## A perfect number is a number for which the sum of its proper divisors 
## is exactly equal to the number. For example, the sum of the proper 
## divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
## A number n is called deficient if the sum of its proper divisors is 
## less than n and it is called abundant if this sum exceeds n.
## As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
## the smallest number that can be written as the sum of two abundant numbers 
## is 24. By mathematical analysis, it can be shown that all integers greater 
## than 28123 can be written as the sum of two abundant numbers. However, 
## this upper limit cannot be reduced any further by analysis even though it is known 
## that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
## Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from pylab import *
import math
import time
start=time.clock()
n=6
result=[]
while n <=28123:
        a=1
        f=math.floor(sqrt(n))
        for i in range(2,int(f)+1):
                if n%i==0:
                        if i!=n/i:
                                a=a+i+n/i
                        if i==n/i:
                                a=a+i
        if a>n: 
                result.append(n)
        n+=1

n=1
s=0
result=asarray(result)
limit=28123
tt=0
a=[]
while n <=limit:
        count=0
        temp=result[result<n]
        for j in range(len(temp)):
                if len(temp[temp==n-temp[j]])==1:
                        count+=1
                        break
        if count==0:
                s+=n
                tt+=1
                a.append(n)
                if tt%100==0: 
                        print s,n
        
        n+=1
end=time.clock()
print(end-start)

