## Problem 21 - Amicable numbers
## Let d(n) be defined as the sum of proper divisors of n (numbers 
## less than n which divide evenly into n).
## If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable 
## pair and each of a and b are called amicable numbers.
## For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 
## 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors 
## of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
## Evaluate the sum of all the amicable numbers under 10000.

import math
n=3
result=[]
while n <=10000:
        count=0
        f=math.floor(sqrt(n))
        a=[]
        for i in range(2,int(f+1)):
                if n % i ==0:
                        a.append(i)
                        a.append(n/i)
        if len(a)>=2:
                temp=sum(a)+1
                f=math.floor(sqrt(temp))
                b=[]
                for j in range(2,int(f+1)):
                        if temp % j==0:
                                b.append(j)
                                b.append(temp/j)
                if n==sum(b)+1 and n!=temp:
                        print(n,temp)
                        result.append(n)
                        result.append(n)
        n+=1
r=set(result)
print (reduce(lambda x,y:x+y, r))

## Answer: 31626

