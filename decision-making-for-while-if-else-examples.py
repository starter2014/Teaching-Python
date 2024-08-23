# The "EMPTY" or "ZERO" or "FALSE"
# The other than above are treated as TRUE, ONE

##x=int(input("Enter Number: "))
##
##if x%2 ==0:
##    print(x,"is even number")

#######################################3
##v=int(input("Enter V Number: "))
##y=int(input("Enter y Number: "))
##
##if v==1:
##    y=y+1
##    print(y)
##else:
##    if v==2:
##        y=y+2
##        print(y)
##    else:
##        if v == 3:
##            y= y+3
##            print(y)
##        else:
##            y = y-10
##            print(y)

## The pass statement does nothing.
## It can be used when a statement is required syntactically
## but the program requires no action. For example:
##x=int(input("Enter x Number: "))
##sum = 0
##if x!=100:
##    sum+=x
##    print(sum)
##else:
##    print(sum)
##    pass
##    #print(sum)
################################
## To check the nature of the integer###############
# write a python program to read an integer and use bitwise operator
# to check the nature(odd or even) of the integer
# Read an integer from the user

##number = int(input("Enter an integer: "))
##
### Use the bitwise AND operator to check if the number is odd or even
##
##if number & 1 == 0:
##    #print(f"{number} is even.")
##    print(number,"is even")
##else:
##    #print(f"{number} is odd.")
##    print(number,"is odd") # different print style
    
########################################
## To find the maximum of three numbers
##num_1 = int(input("Enter an integer1: "))
##num_2 = int(input("Enter an integer2: "))
##num_3 = int(input("Enter an integer3: "))

##max_no = num_1
##
##if max_no < num_2:
##    max_no = num_2
##else:
##    #max_no = num_1
##    pass
##if max_no < num_3:
##    max_no = num_3
##else:
##    pass
##print ("Maxium of three number is: ",max_no)

#ooooooooorrrrrrrrrrrrrrrr##
##max_no = 0
##if num_1>= num_2 and num_1>= num_3:
##    max_no = num_1
##elif num_2 >= num_1 and num_2 >= num_3:
##    max_no = num_2
##else:
##    max_no= num_3
##print ("Maxium of three number is: ",max_no)

#-------------------------------------#


## find the distance between two point of the plane

import math

# Input: Read the coordinates of the first point (x1, y1)

x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))

# Input: Read the coordinates of the second point (x2, y2)

x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

# Distance calculation
## pow(2,3) - 2 power 3 or pow(x,y) - x to the power y
## 8
#distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
distance = math.sqrt(pow((x2 - x1),2) + pow((y2 - y1),2))
           
print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")
