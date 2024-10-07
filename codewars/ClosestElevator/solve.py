""" 

Condition: Given 2 elevators (named "left" and "right") in a building with 3 floors (numbered 0 to 2), write a function elevator accepting 3 arguments (in order)

Target: Return the closest floor with the call floor.

Details: In the case where both elevators are equally distant from the called floor, choose the elevator to the right.

"""


def elevator(left, right, call):
    
    # set Distance between call floor and right or left floor, using abs function to evade negative result.
    rightDistance = abs(call - right)
    leftDistance = abs(call - left)

    # checks the distance
    if rightDistance > leftDistance:
        return "left"
    else:
        return "right"
