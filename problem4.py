#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
import math
side1=float(input("enter the length of side1:"))
side2=float(input("enter the length of side2:"))
side3=float(input("enter the length of side3:"))
hypotenuse=max(side1,side2,side3)
expected_hypotenuse=math.sqrt(side1**2+side2**2)
percent_dif=abs(expected_hypotenuse-hypotenuse)/expected_hypotenuse*100
if percent_dif<2:
    print ("the side length are close enough to make a right triangle.")
else:
    print("the side length do not form a right triangle")