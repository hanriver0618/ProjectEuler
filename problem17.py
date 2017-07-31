## Problem 17 - Number letter counts
## If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
## then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
## If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
## in words, how many letters would be used?

## NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
## contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
## The use of "and" when writing out numbers is in compliance with British usage.

from pylab import *
import time
import math
start=time.clock()

name=['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen',
name1=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
num=0
for i in range(1,1001):
        a=0
        b=0
        c=0
        if i <= 19:
                c=name[i-1]
                c=len(c)
        if 20<=i<=99:
                b=name1[int(math.floor((i)/10.-2))]
                b=len(b)
                if i%10!=0:
                        c=name[i%10-1]
                        c=len(c)
        if 100<=i<=999:
                a=name[i/100-1]
                if i%100==0:
                        a=len(a)+7
                else:
                        a=len(a)+7+3

                if 1<=i%100 < 20:
                        c=name[i%100-1]
                        c=len(c)
                if 20<=i%100<=99:
                        b=name1[int(math.floor((i%100)/10.-2))]
                        b=len(b)
                        if (i%100)%10!=0:
                                c=name[(i%100)%10-1]
                                c=len(c)
        if i==1000:
                a='onethousand'
                a=len(a)
        num+=a+b+c
        print num,i,a,b,c
print num
end=time.clock()
print end-start

## Answer: 21124
