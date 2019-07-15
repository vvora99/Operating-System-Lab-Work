import math

head=int(input("Enter Head"))

n=int(input("Enter n"))

list1=[]
for i in range(n):
    list1.append(int(input("Enter page "+str(i+1)+" ")))

templi=list1[:]

cost=0
for i in range(n):
    diff=[]
    for val in templi:
        diff.append(abs(head-val))
    mindiff=min(diff)
    mindiffindex=diff.index(mindiff)
    cost+=mindiff
    head=templi[mindiffindex]
    templi.remove(templi[mindiffindex])
print(cost)
