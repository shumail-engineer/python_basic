# circumcentance of circle :

import math
r = float(input("enter radius of circle: "))
x = math.pi
circumcentance = 2*x*r
print(f"the circumctance of circle is {round(circumcentance,2)}")

# radius of circle

radius = float(input("Enter radius of circle: "))
Area = math.pi*pow(radius,2)
print(f"The area of circle is {round(Area,2)}")

#hypotenious of circle:

a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c =  pow(a,2) + pow(b,2)
d = math.sqrt(c)
print(f"the hypotenious of right triangle is {round(d,2)}")
