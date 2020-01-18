"""
print("Hello World")
print("This is a string")
print("123 ABC")# Anything in quotes is a string
print('123') #single apostrophies work too
print('123A')
print("123A")

#Pringing Numbers
print(7) #This is an intiger
print(3.14) #This is a float
print(-897)

#printing Booleans
print(True)
print(False)

"""
"""
This is a multi-line comment
This is still part of
the comment
"""
"""
# Basic Math
print(8+3)
print(8-5)
print(8*3) # shift+8 to get the asterisk
print(10/3)
# Semi-Advanced Math
# Powers or Exponents
print(3**1)
print(1**3)
# Floor Division
# Ignored remainders or decimals
print(11//5)
print(77//10)
print(102//25)

# Remainder
# Also called 'MOD'
print(11%5)
print(78%10)

# Creating Variables
my_fav_num = 63
print(my_fav_num)
name = "John Doe"
print("Welcome " + name)
print(name)
# Updating Variables
price = 7
price += 3
print(price)
cost = 50
cost -= 10
print(cost)

# Writing a code segment
small = 12
medium = 15
large = 20
small = large - medium
large = large % small
medium = large - small
print(small)
print(medium)
print(large)
m1=25
m2=15
m2!=2
print(8<3)
print(8>3)
print(8<=3)
print(8>=3)
print(8==3) # double checks if equal
print(8!=3) #means not

print(3.14*5**2*10)
# Manipulating String Cases
my_name = "sam"
my_name = my_name.upper()
color = "PURPLE"
color = color.lower()
state = "califORNIA"
state = state.title()
print(my_name, color, state)
# Concatenating (Joining) Strings
first = "Rey "
last = "G"
full = first + last
sentence = "Welcome " + full + " to CSE!"
print(sentence)
# Taking User Input as a String
name = input("Enter your name : ")
print(type(name))
print(name)

age = input("Enter your age: ")
print(type(age)) # still a string
age = int(age) # turn it into an integer, if we can
print(type(age))
print(age)
# String Formatting
# Places the values of the variables at the end into each curly bracket {} in order
print("Welcome {}!".format(name))
print("Welcome {}! You are {} years old!".format(name, age))
"""


# Typecasting

value = int(input("enter a number"))
cost = 12
print(value+cost)

print("7" + "5")
print(int("7") + int("5"))
print(str(7)+str(5))