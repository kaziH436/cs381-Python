# Keyword arguments are evaluated in the same order as they are passed in
# with a value and the order doesn't matter 

# Posiitional arugment 
# without a value

# forcing the a keyword
# * menas there needs to be a value focing keyword arugment: required 
# but args* is optional: variatic 
# scale=1 is a default argument, optional as well 

# **prams: variatic args that store this as a dict 

# how does .pop work for dict in python?

# Docorators
def my_decorator(func):
 def wrapper():
    print("Something is happening before the function is called.")
    func()
    print("Something is happening after the function is called.")
 return wrapper

@my_decorator
def say_hello():
    print("Hello!")
say_hello()
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

# If. a fucntion is a docartor, a function object will be created 