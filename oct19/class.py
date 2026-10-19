import sys 

# a=[1,2,3]
# sys.getrefcount(a) # prints 2 since 

# b=a
# sys.getrefcount(a) # prints 3, since getrefcount is a pointer

# sys.getrefcount(a) # prints 2


a=[1]
b=[2]
c=[3]
sys.getrefcount(a)
sys.getrefcount(b)
sys.getrefcount(c)
d=[a,b,c]
sys.getrefcount(d)
d.clear()
print(d)
sys.getrefcount(a)


a=1
b=2
c=3
d=[a,b,c]
for i in d: # i becomes a reference and when del i, i breaks its own reference. The original list is untouched 
    del i # deletes each elememt from d
print(d) # [1, 2, 3], 