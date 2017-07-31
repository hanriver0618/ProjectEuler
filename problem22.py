## Problem 22 - Names scores
## Using names.txt (right click and 'Save Link/Target As...'), 
## a 46K text file containing over five-thousand first names, begin by sorting 
## it into alphabetical order. Then working out the alphabetical value for 
## each name, multiply this value by its alphabetical position in the list to obtain a name score.
## For example, when the list is sorted into alphabetical order, COLIN, 
## which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
## So, COLIN would obtain a score of 938 × 53 = 49714.
## What is the total of all the name scores in the file?


from pylab import *
f=open("data22.dat")
for line in f:
        print(line)
string='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
line=sort(line.split(","))
line=line.tolist()

list_string=list(string)
number=range(1,27)

for j in range(len(line)):
        for i in range(26):
                 line[j]=line[j].replace(list_string[i],' '+str(number[i])
#line=line.split(",")
sum=0 
for i in range(len(line)): 
        temp=reduce(lambda a,b:a+b,map(int,line[i][1:-1].split()))
#       if map(int,line[i][1:-1].split())==[3,5,12,9,14]:
        sum+=(i+1)*temp
        print((i+1),sum,line[i],temp,map(int,line[i][1:-1].split()))
print(sum)

