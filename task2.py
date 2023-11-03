#! python3
"""
 Have the user input a number 
 Determine if the number is positive, negative or 0 
 2 points

 Inputs:
 number

 Outputs:
 - "positive"
 - "negative"
 - "zero"

 Example:

Enter a number: 3
positive

Enter a number: -1.2
negative
"""
x = int(input("enter a number"))
if x==0:
    print("the number is zero")
elif x < 0:
     print("the number is negative")
elif x > 0:
    print("the number is larger then 0")
