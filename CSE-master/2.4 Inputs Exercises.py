# 1
"""
first = input("Enter your first name: ")
last = input("Enter your last name: ")
print("Welcome {} {}! How is your day?".format(first,last))
"""
# 2
"""

from datetime import datetime
now = datetime.now()
if now.strftime("%H") > "12":
    AmPm = "AM"
else:
    AmPm = "PM"

current_time = now.strftime("%H:%M ")
print("Current Time =", current_time + AmPm)
"""
# 3
"""
first = input("Enter your first name: ")
last = input("Enter your last name ")
street = input("Enter your street name (ex. 123 N Normal): ")
streettype = input("Enter your street type (avenue, street, court, etc.): ")
city = input("Enter your city: ")
state = input("Enter your state(ex. CA): ")
zip = input("Enter your zip code: ")
print("{} {}".format(first,last))
print("{} {}".format(street,streettype))
print("{}, {} {}".format(city,state,zip))
"""
# 4
"""
cls1 = input("Enter your first class (English,Math, etc.): ")
grd1 = input("Enter your grade in your first class (A,B,C,D): ")
cls2 = input("Enter your second class (English,Math, etc.): ")
grd2 = input("Enter your grade in your second class (A,B,C,D): ")
cls3 = input("Enter your third class (English,Math, etc.): ")
grd3 = input("Enter your grade in your third class (A,B,C,D): ")
cls4 = input("Enter your fourth class (English,Math, etc.): ")
grd4 = input("Enter your grade in your fourth class (A,B,C,D): ")
cls5 = input("Enter your fifth class (English,Math, etc.): ")
grd5 = input("Enter your grade in your fifth class (A,B,C,D): ")
cls6 = input("Enter your sixth class (English,Math, etc.): ")
grd6 = input("Enter your grade in your sixth class (A,B,C,D): ")
grd1 = str(grd1)
grd2 = str(grd2)
grd3 = str(grd3)
grd4 = str(grd4)
grd5 = str(grd5)
grd6 = str(grd6)
print("Class 1:{}          Grade: {}".format(cls1,grd1))
print("Class 2:{}          Grade: {}".format(cls2,grd2))
print("Class 3:{}          Grade: {}".format(cls3,grd3))
print("Class 4:{}          Grade: {}".format(cls4,grd4))
print("Class 5:{}          Grade: {}".format(cls5,grd5))
print("Class 6:{}          Grade: {}".format(cls6,grd6))
if grd1=="A":
    grd1 = 4
elif grd1 == "B":
    grd1 = 3
elif grd1 == "C":
    grd1 = 2
elif grd1 == "D":
    grd1 = 1

if grd2 == "A":
    grd2 = 4
elif grd2 == "B":
    grd2 = 3
elif grd2 == "C":
    grd2 = 2
elif grd2 == "D":
    grd2 = 1

if grd3 == "A":
    grd3 = 4
elif grd3 == "B":
    grd3 = 3
elif grd3 == "C":
    grd3 = 2
elif grd3 == "D":
    grd3 = 1

if grd4 == "A":
    grd4 = 4
elif grd4 == "B":
    grd4 = 3
elif grd4 == "C":
    grd4 = 2
elif grd4 == "D":
    grd4 = 1

if grd5 == "A":
    grd5 = 4
elif grd5 == "B":
    grd5 = 3
elif grd5 == "C":
    grd5 = 2
elif grd5 == "D":
    grd5 = 1

if grd6 == "A":
    grd6 = 4
elif grd6 == "B":
    grd6 = 3
elif grd6 == "C":
    grd6 = 2
elif grd6 == "D":
    grd6 = 1

print("Your Semester GPA:  {}".format(grd1+grd2+grd3+grd4+grd5+grd6/6))
"""
# 5
"""
L = input("Insert the length of the rectangle: ")
W = input("Insert the width of the rectangle: ")
L = (int(L))
W = (int(W))
print("The area of your rectangle is {}".format(L*W))
print("The perimeter of your rectangle is {}".format(L+L+W+W))
"""
# 6
"""
L1 = input("Insert the length of one side of your triangle: ")
L2 = input("Insert the length of the other side of your triangle: ")
L1 = int(L1)
L2 = int(L2)
L3 = int(L1**2+L2**2)**.5
print("The length of the hypotenuse in your triangle is {}".format((L1**2+L2**2)**.5))
print("The perimeter of your triangle is {}".format(L1+L2+L3))
"""
# 7
"""
LRP = input("Enter the length of your rectangular prism: ")
HRP = input("Enter the height of your rectangular prism: ")
WRP = input("Enter the width of your rectangular prism: ")
LRP = int(LRP)
HRP = int(HRP)
WRP = int(WRP)
print("The volume of your rectangular prism is {}".format(LRP+HRP+WRP))
print("The surface area of your rectangular prism is {}".format(2*(WRP*LRP+HRP*LRP+HRP*WRP)))
"""
# 8
"""
R = input("Enter the radius of your cylinder: ")
H = input("Enter the height of your cylinder: ")
R = int(R)
H = int(H)
π = 3.14159265359
print("The volume of your cylinder is {}".format(π * R ** 2 * H))
print("The surface area of your cylinder is {}".format(2*π*R*H+2*π*R**2))
"""
# 9
"""
x = input("This is the f(x)=(x+1)*(x+2) and f(x)=(x+1)/(x+2) calculator please input x: ")
x = int(x)
print("f(x)={}".format((x+1)*(x+2)))
print("f(x)={}".format((x+1)/(x+2)))
"""
# 10
"""
print("This is the quadratic formula calculator")
a = input("please input \"a\" for your quadratic formula: ")
b = input("please input \"b\" for your quadratic formula: ")
c = input("please input \"c\" for your quadratic formula: ")
a = int(a)
b = int(b)
c = int(c)
print("x={}".format(((-b + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a))))
print("x={}".format((-b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)))
"""
cost = 100
cost /= 2
print("Hello" + "World" , "cost")
str(cost)
print("EEEEEEEEEEE\t\tEREEEEEEEEEEEE")
