# x=float(input("Enter the number of hours worked: "))
# y=float(input("Enter your hourly rate: "))

# z=(x <= 40) * y + (x>40) * (int(x) - 40) * y
# print("straight time pay: $", format(z, "0.2f"))

# overtime_pay = (x > 40) * (int(x) - 40) * float(y) * 1.5
# print("overtime pay: $", format(overtime_pay, "0.2f"))


# total_pay = z + overtime_pay
# print("total pay: $", format(total_pay, "0.2f"))



# x=float(input("please enter an integer number: "))
# s = "even"
# if x % 2 != 0:
#     s = "odd"
# print(x, "is", s)



# n= input("Enter a number 1, 2 or 3: ")

# if n == "1":
#     print("The color is red")

# if n == "2":
#     print("The color is green")

# if n == "3":
#     print("The color is blue")

# if n != "1" and n != "2" and n != "3":
#     print("ERROR!")


# x = float(input("enter an integer: "))
# y = float(input("enter an integers: "))
# z = float(input("enter an integers: "))
# w = float(input("enter an integers: "))
# v = float(input("enter an integers: "))

# maximum = x
# if y > maximum:
#     maximum = y
# if z > maximum:
#     maximum = z
# if w > maximum:
#     maximum = w 
# if v > maximum:
#     maximum = v
# print("The maximum number is:", maximum)


x = float(input("enter an grade number: "))

if x >= 90:
    print("Your grade is A")
elif x >= 80:
    print("Your grade is B")
elif x >= 70:
    print("Your grade is C")
elif x >= 60:
    print("Your grade is D")
elif x >= 0:
    print("Your grade is F")
else: 
    print("Score out of range")