import math
n=int(input("Enter no. : "))

head = int(input("Enter head start : "))
li=[]
for i in range(n):
	x = int(input("enter " + str(i+1) + " : " ))
	li.append(x)
print(li)
c=0
for i in range(n):
	pre = li[i]
	t = abs(head - pre)
	head = pre
	c+=t
print(c)
