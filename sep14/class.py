#print(a=9) #print() got an unexpected keyword argument 'a', 
# print(a:=1) # prints 1, the walrus operator assigns 1 to a and returns it

# x=int(input("Enter a number: "))
# print(x%2==0) # prints True if x is even, False if x is odd
# x=int(input("Enter a number: "))
# print(x, "is", (x%2==0) * "even" + (x%2==1) * "odd")# prints even if x is even, odd if x is odd

# a, b = 1, 2
# print(a, b) # prints 1 2
# tmp=a
# a=b 
# b=tmp
# print(a, b) # prints 2 1
# a,b = b,a
# print(a, b) # prints 2 1


#format(expr, spec), expression has a value and a sideeffect 

# s="hello \n world"
# print(str(s)) # prints 
# # hello 
# #  world
# print(repr(s)) # prints 'hello \n world'
# print(s) # prints 
# # hello 
# #  world


# x = input("please enter the number of hours that you worked: ")
# #print(format(float(x), "0.1f")) # prints the number of hours that you worked with 1 decimal places
# y = input("please enter you houely rate: ")
# #print(format(float(y), "0.1f")) 
# print( "You earned $", format(float(x) * float(y), "0.2f"), "for ", x, "hours of work at ", format(float(y), "0.2f"), "/hour") # prints the amount of money that you earned with 2 decimal places

# print(f"You earned ${float(x) * float(y):0.2f} for {x} hours of work at ${float(y):0.2f}/hour") 
# # prints the amount of money that you earned with 2 decimal 

x=input("enter some amount of money: ")
# Output: Your program should output the minimum number of coins required to render the amount entered
# into coins. The coins are half-dollars, quarters, dimes, nickels and pennies.
# Your program should also list how many of each coin needs to be provided. Each denomination on its own
# line, starting with half-dollars.
arr = [50, 25, 10, 5, 1]
coins=0
for i in arr:
    coins += x // i
    x = x % i   
print("Minimum number of coins required:", coins)