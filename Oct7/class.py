# Functions are objects

# closure is a function that is defined inside another function and has access to the variables of the outer function.
# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function



# def Dog():
#     def bark():
#         print('Woof!')
#     Dog.bark = bark # bark is an attribute of Dog, bark is a pointer to the bark function
#     return Dog 

# # bark() # gives an undefined error, since bark() under Dog 
# # Dog.bark() # no attribute error when Dog.bark() is called


# spot = Dog() # spot is an instance of Dog class, the body of Dog() is run
# # spot.bark() # when spot.bark() is called, woof! will be printed
# spot.bark # doesn't print but returns a pointer to the bark function 


# def Dog():
#     def bark():
#         print('Woof!')
#     Dog.bark = bark
#     return Dog 

# Dog()
# Dog.bark() # prints woof! since Dog.bark() is called after Dog() is called, so bark() is defined and assigned to Dog.bark


# Arguments
# def add(x,y):
#     return x+y 
# a=1
# print(add(a,a+1)) # arguments are evaluated first,prints 3


# def f(x, items=[]): # default argument is mutable and is evaluated only once when the function is called, not each time the function is called
#     items.append(x)
#     return items
# f(1) # [1]
# f(2) # [1, 2]
# f(3) # [1, 2, 3]

# def func(x, items=None): # default argument is immutable and is evaluated each time the function is called
#     if items is None:
#         items = []
#     items.append(x)
#     return items

# print(func(1)) # [1]
# print(func(2)) # [2]
# print(func(3)) # [3]

# Variatic arguments: the number of args when calling the function vaires
# sum(1,2) # 3
# sum(1,2,3) #TypeError: sum() takes at most 2 arguments (3 given)
# sum([1,2,3]) # not variatic



# def sum(*args): 
#     pass

k=sum
def sum(*args): 
    pass
print(k([1,2,3,4,5])) # uses built in sum not the function sum defined