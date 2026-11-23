# Yes, there is a significant difference.
# First line: x = (a = 5) → SyntaxError: invalid syntax. This is a syntax error because the = operator (assignment) cannot be used inside parentheses without the walrus operator :=. Standard assignment = is a statement, not an expression.
# Second line: x = a = 5 → Valid. This is chained assignment. Both x and a are assigned the value 5.
# Explanation: The first line would need to use the walrus operator to work: x = (a := 5), which assigns 5 to a and then assigns that value to x.




# Approach 1: print(a = 7) → SyntaxError: invalid syntax. This is invalid because = is used for assignment, which is a statement, not an expression. It cannot be used as an argument to a function.
# Approach 2: print(a := 7) → Output: 7. This works correctly. The walrus operator := is an assignment expression that assigns 7 to a and also returns the value 7, which is then printed. The variable a is created with the value 7.
# Explanation: The key difference is that := (walrus operator) is an expression that returns a value, while = is only a statement that doesn’t return a value.




# while input_str := input("Enter text: "):
#     print(input_str) Does this while loop, does it exit when the input string does not exist, or does it exit when the input string is empty? Because if it's empty, it still exists, so it should not exit. But like, it should exit if the input string is none, for example, it doesn't exist.
# Python's while doesn't test existence. It tests whether the value is truthy. The falsy values are "", 0, None, [], {}, and False. So when the user just presses Enter, input() returns "", the walrus operator assigns that to input_str, the condition evaluates to falsy, and the loop ends. The variable does exist at that point (it holds an empty string), but that doesn't matter.
# Also, input() never returns None. It always returns a string, so the "None" case can't happen here.




print("{} {} {}".format("seven", "eight", "nine"))
# Output: seven eight nine
# Explanation: The {} placeholders are filled sequentially with the positional arguments in order. The first {} gets “seven”, the second gets “eight”, and the third gets “nine”.




# Output:

# True
# False
# False
# False

# Explanation: In Python, an object is considered falsy if it is:

# None
# False
# Zero (0, 0.0, 0j)
# Empty sequences or collections (”, [], {}, (), set())
# Anything else is truthy.

# bool('False') → True: The string 'False' is non-empty, so it’s truthy (even though it contains the word “False”).
# bool('') → False: An empty string is falsy.
# bool(0.0) → False: Zero (as a float) is falsy.
# bool([]) → False: An empty list is falsy.





# Output:

# 2.0
# 2
# -3.0
# -2

# Explanation: The key difference is in how they handle negative numbers:

# // is floor division: it rounds towards negative infinity.
# int() truncates towards zero.
# For positive numbers, they behave the same way:

# 2.9 // 1 = 2.0 (floor division rounds down)
# int(2.9 / 1) = 2 (truncates towards zero)
# For negative numbers, they differ:

# -2.9 // 1 = -3.0 (floor division rounds down to -3)
# int(-2.9 / 1) = -2 (truncates towards zero to -2)
# Also note that // returns a float when one operand is a float, while int() always returns an integer.