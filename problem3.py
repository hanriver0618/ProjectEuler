## Problem 3 : <Largest prime factor>
## The prime factors of 13195 are 5, 7, 13 and 29.
## What is the largest prime factor of the number 600851475143 ?
const=600851475143
fix_const=const
a=[]
for i in range(int(fix_const/2)):
	if const % (i+2) ==0:
		a.append(i+2)
		const=const/(i+2)
	while const % (i+2)==0:
		const=const/(i+2)
		print(const)
	if const==1:
		break
print(a)

## Answer : 6857 

