"""

Condition: You forgot to count the number of toast you put into there, you don't know if you put exactly six pieces of toast into the toasters.
Target: Define a function that counts how many more (or less) pieces of toast you need in the toasters. Even though you need more or less, the number will still be positive, not negative.
Details: You must return the number of toast the you need to put in (or to take out). In case of 5 you can still put 1 toast in:

""" 

def six_toast(num):

    # return the less or 
    return abs(num - 6)

print(six_toast(3))