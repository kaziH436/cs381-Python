
# a=1
# b=2
# c=3
# d=[a,b,c]

# for i in range(len(d)-1,-1,-1):
#     print(d)
#     if i%2==0:
#         del d[i] 
# print(d)




# def my_clear(lst):
#  for i in range(len(lst) - 1, -1, -1):
#     del lst[i]
# a = [1, 2]
# b = [3, 4]
# c = [a, 5, b, 6]

# # Using my_clear
# my_clear(c)



# for i in range(len(d)-1):
#     print(d)
#     del d[i]

# if d:
#     del d[len(d)-1]
# print(d)


# for i in range(len(d)):
#     print(d)
#     del d[0] # breaks the refereence between the objects 1,2,3 and the pointer to 1,2,3
# print(d)


# sum=0
# res=[]
# for i in range(1,11):
#     res.append(i)
#     sum+=i
# print(res, sum)

import random as r 
res=[]
for i in range(10):
    res.append(r.randint(1,10))
print(res)