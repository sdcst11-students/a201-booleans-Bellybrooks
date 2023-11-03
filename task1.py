#! python3

"""
Have the user input a number. 
Determine if the number is larger than 100 
If it is, the output should read "The number is larger than 100" 
(2 points)
Inputs:
number
Outputs:
"The number is larger than 100"
"The number is smaller than 100"
"The number is 100"

Example:
Enter a number: 100
The number is 100

Enter a number: 102
The number is larger than 100
"""

x = int(input("enter a number"))
if x==100:
    print("the number is = to 100")
elif x > 100:
     print("the number is larger then 100")
elif x < 100:
    print("the number is smaller then 100")
