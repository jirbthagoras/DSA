""" 

Condition: Given sets of words
Target: Reverse the set of word
Detail: Words are separated by space

"""

def reverse_words(s):

    # first, explode the string into array
    # second, reverse the array
    # third, implode the array into string

    return " ".join(s.split()[::-1])

print(reverse_words("halo guys"))