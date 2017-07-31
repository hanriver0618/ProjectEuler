## Problem 4 - Largest palindrome product
## A palindromic number reads the same both ways. 
## The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
## Find the largest palindrome made from the product of two 3-digit numbers.

## palindromic number

a=999
b=999
break_result=0
for i in reversed(range(a)):
	for j in reversed(range(b)):
		result=i*j
		temp=list(str(result))
		if temp==temp[::-1]:
			if break_result < result:
				break_result=result
				break
print(break_result)

## Answer: 906609

