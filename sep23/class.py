# x=int(input("Enter a 4 digit string: "))
# last_digit=x%10
# first_digit=x//1000
# if x> 999 and x<10000:
#     last_digit=x%10
#     first_digit=x//1000

# print(f"Yes, {x} is a palindrome number") if first_digit==last_digit else print(f"No, {x} is not a palindrome number")


# reversing a three digit number 
# x=int(input("Enter a three digit number: "))

# last_digit=x%10
# x=x//10
# middle_digit=x%10
# first_digit=x//10

# print(f'{last_digit}{middle_digit}{first_digit}')




# x=int(input("Enter a three digit number: "))
# last_digit=x%10
# x=x//10
# middle_digit=x%10
# first_digit=x//10
# result=x%10*100+x%100*10+x//10
# print(f'{result}')



# n= int(input("Enter a number: "))
# while n>0:
#     print(n)
#     n-=1

    
# n= int(input("Enter a number: "))
# i=1
# count=0
# while i<=n:
#     if i%2==0:
#         print(i, end=" ")
#         count+=1 
#         if count==5:
#             print()
#     i+=1


# n= int(input("Enter a number: "))
# i=1
# count=0
# while i<=n:
#     if i%2==0:
#         print(i, end=" ")
#         count+=1 
#         if count==5:
#             print()
#     i+=1


# x=int(input("Enter a number: "))
# i=1

# while i<=x:
#     print("*"*i)
#     i+=1


# n = int(input("Enter a number: "))
# i=1
# ans = 0
# while i<=n:
#     ans += i
#     i+=1
# print(ans)



# a=[1,2,3,4,5]
# sum=19
# print(sum(a)) #prints a key error becuase all functions are pointers in python and sum=19 reassigned the pointer  function sum 



password=int(input("Enter a password: "))
while password:
    last_diigt=password%10
    first_digit=password//10
    if first_digit%2==0 and last_diigt%2==0:
        print("valid")
        break
    else:
        print(input("invalid! Enter a password: "))
        break
      