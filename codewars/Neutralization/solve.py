"""

Condition: Given 2 strings, s1 and s2.

Target: Return a new string which shows how the two given string interacts

Details:
- When positives and positives interact, they remain positive.
- When negatives and negatives interact, they remain negative.
- But when negatives and positives interact, they become neutral, and are shown as the number 0.


"""


def neutralise(s1, s2):

    # Set variable for the answer
    answer = ""

    # Use for loop to iterate through given string
    for x in range(len(s1)):
        # if pair of char is the same, append the same character in the ans variable
        if s1[x] == s2[x]:
            ans += s1[x]
        # else? it will add zero
        else:
            ans += "0"       
    return answer

print(neutralise("-++++", "+++--"))