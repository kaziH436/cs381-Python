def shout(text):
 return text.upper()
def whisper(text):
 return text.lower()
def greet(func):
 greeting = func("Hello, I am a function")
 print(greeting)
greet(shout) # Output: "HELLO, I AM A FUNCTION"
greet(whisper) # Output: "hello, i am a function"



# A closure in Python is a function object that remembers values in enclosing scopes even if they
# are not present in memory. It is a record that stores a function together with an environment: a
# mapping associating each free variable of the function with the value or reference to which the
# name was bound when the closure was created.

