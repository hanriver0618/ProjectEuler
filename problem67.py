## Problem 67 - Maximum path sum II
## By starting at the top of the triangle below and moving to adjacent 
## numbers on the row below, the maximum total from top to bottom is 23.
## 3
## 7 4
## 2 4 6
## 8 5 9 3
## That is, 3 + 7 + 4 + 9 = 23.
## Find the maximum total from top to bottom in triangle.txt (
## right click and 'Save Link/Target As...'), a 15K text file containing 
## a triangle with one-hundred rows.
## NOTE: This is a much more difficult version of Problem 18. It is not 
## possible to try every route to solve this problem, as there are 299 
## altogether! If you could check one trillion (1012) routes every second 
## it would take over twenty billion years to check them all. 
## There is an efficient algorithm to solve it. ;o)


from pylab import *
 
f=open('data67.dat')
a=[map(int,line.split()) for line in f]
 
def triange(a):
	while len(a) <=1:
		a0=a.pop()
		a1=a.pop()
		a.append(max(a0[i],a0[i+1])+t for i,t in enumerate(a1))
		return a[0][0]

## Answer: 7273

