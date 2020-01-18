#Rounding with .format()
#Method 1: Storing value in a variable
num1 = 22/7
print("{:.2f}".format(num1))
print("{:.3f}".format(num1))
print("{:.4f}".format(num1))
print("{:.5f}".format(num1))
num2 = 33/7
print("{:.3f}".format(num2))
print("{:.6f}".format(num2))
print("{:.4f}".format(num2))
num3 = 17/5
print("{:.2f}".format(num3))
print("{:.0f}".format(num3))
num4 = 10101/17
print("{:.4f}".format(num4))
print("{:.5f}".format(12345/45))

#escape characters
# Change automatic formating

sent1 = "This is my sentence"
print(sent1)
#New Line
sent1 = "This \nis \nmy sentence"
print(sent1)
#New Line
sent1 = "This \t is \t my sentence"
print(sent1)

sent2 = "She said \"yes\" to her mom"
print(sent2)

sent3 = 'Jack\'s dog '
print(sent3)

sent4 = "Jill's dog"
print(sent4)

sent5 = 'My "dog"'
print(sent5)



"""
print("This \t is \t my \t string.")

print("This \n is \n SPARTA.")

print("Sally said \"no\" about the jacket.")
print("Sally said "no" about the jacket.")

print('This is Sally\'s jacket.')
print('This is Sally's jacket.')

print("I used years \\ months")
"""

perimiter = 2*5+2*10
print("We need",      perimiter,     "feet of fencing for the yard")

print("{:2f}".format(2.2497))