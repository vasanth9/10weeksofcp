#if else elif
a=100
b=200
if a==20:
    print("20")
elif a==100:
    print("100")
else:
    print("nothing")

#short hand
print("A") if a>b else print("B")
"""
100
B
"""
#while Loop
i=1
while i<3:
    print(i)
    i+=1
    if(i==2):
        break
print("break at ",i)
i=0
while i<9:
    i=i+1
    if i==3:
        continue
    print(i)   
else:
    print("out yeee")
"""
1
break at  2
1
2
4
5
6
7
8
9
out yeee
"""

#for loop

for x in "banana":
    print(x)
for x in range(6):
    print(x)
for x in range(3,7):
    print(x)
for x in range(2,18,3):
    print(x)

#we can also use break,continue and pass

"""
b
a
n
a
n
a
0
1
2
3
4
5
3
4
5
6
2
5
8
11
14
17
""" 






