""" 

Condition:
Given three integers a, b, and c, return the largest number obtained after inserting the operators +, *, and parentheses (). In other words, try every combination of a, b, and c with the operators, without reordering the operands, and return the maximum value.

Target: return highest value

"""

import math

def expression_matter(a, b, c):

    # Enters all operands in in the array, and select the highest value.
    # Somehow, this question's information is not good detailed.
    # The operation a + b + c is not shown in the question.
    
    return max(a + b + c,a * (b + c), a * b * c, a + b * c, (a + b) * c)

print(expression_matter(1, 1, 1))