#arithmatic operations +,-,*,/,//,%
x=3
y=10

print(x+y)
print(x-y)
print(x*y)
print(y**x)
print(y/x)
print(y%x)
print(y//x)

"""
13
-7
30
1000
3.3333333333333335
1
3
"""

#assignment operations =,+=,-=,*=,/=,%=,//=,**=,&=,|=,^=,>>=,<<=
x=5
print(x)
x+=3
print(x)
x-=3
print(x)
x*=3
print(x)
x%=9
print(x)
x//=5
print(x)
x/=7
print(x)
x**=2
print(x)
x=100
x&=3
print(x)
x|=5
print(x)
x^=88
print(x)
x>>=2
print(x)
x<<=2
print(x)
"""
5
8
5
15
6
1
0.14285714285714285
0.02040816326530612
0
5
93
23
92
"""

#comparison operations  ==,!=,>,<,>=,<=

x=3
y=4
z=3
print(x==y)
print(x!=y)
print(y>z)
print(x<z)
print(y>=z)
print(x<=z)
"""
False
True
True
False
True
True
"""

# logical operators and,or,nor

x=10
y=4
print(x and y)
print(x or y)
print(not y)
"""
4
10
False
"""

#identity operators is , is not
#same object detection

x="hanuman"
y="hanuma"
z=x
print(x is y)
print(x is z)
print(x is not y)
"""
False
True
True
"""

#membership operators in,not in

x=["hola","ola"]
print("ola" in x)
print("nola" in x)
print("ola" not in x)
"""
True
False
False
"""

#bitwise operators &,|,^,~,>>,<<

x=100
y=300
print(x&y)
print(x|y)
print(x^y)
print(~x)
print(x>>2)
print(x<<2)

"""
36
364
328
-101
25
400
"""

