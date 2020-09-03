import datetime as dt
x=dt.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A")) 
print(x.strftime("%a")) 
print(x.strftime("%w"))
print(x.strftime("%d"))
print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%m"))
print(x.strftime("%y"))
print(x.strftime("%Y"))
print(x.strftime("%H"))
print(x.strftime("%l"))
print(x.strftime("%p"))
print(x.strftime("%M"))
print(x.strftime("%S"))
print(x.strftime("%f"))
print(x.strftime("%z"))
print(x.strftime("%Z"))
print(x.strftime("%j"))
print(x.strftime("%U"))
print(x.strftime("%W"))
print(x.strftime("%c"))
print(x.strftime("%x"))
print(x.strftime("%X"))
print(x.strftime("%%"))


y=dt.datetime(2020,9,3)
print(y)



"""
2020-09-03 12:11:28.460899
2020
Thursday
Thu
4
03
Sep
September
09
20
2020
12
12
PM
11
28
460899


247
35
35
Thu Sep  3 12:11:28 2020
09/03/20
12:11:28
%
2020-09-03 00:00:00
"""