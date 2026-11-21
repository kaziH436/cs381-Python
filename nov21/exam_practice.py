# Write a function lastThenFirst(x) that takes a list x as above and returns a list with the
# sublists listed sorted by last name then first so if a = [['zabie','Gaker'], ['Zable','Aaker']] the
# lastThenFirst(a) will return the list: [['Zabie', 'Aaker'], ['Zable','Gaker']]
import ast
x=ast.literal_eval(input())

def lastThenFirst(x):
    fixed = [[first.capitalize(), last.capitalize()] for first, last in x]

    ans=sorted(fixed, key=lambda name: (name[1],name[0]))
    print(ans)
    return ans

lastThenFirst(x)