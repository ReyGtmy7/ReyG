# Challenge 3
"""
one = int(input("Enter the first number: "))
two = int(input("Enter the second number: "))
if one == two:
    print("You have entered the same number twice")
    pass
three = int(input("Enter the third number: "))
if two == three or one == three:
    print("You have entered the same number twice")
elif one > two and one > three:
    print(str(one) + " is the biggest number")
elif two > one and two > three:
    print(str(two) + " is the biggest number")
elif three > one and three > two:
    print(str(three) + " is the biggest number")
"""
# Challenge 4
grade = "-"
questions = int(input("How many questions were on your test: "))
correct = int(input("How many questions did you get right on your test: "))
percent = (correct/questions)*100
print(percent)
print(grade)
if percent < 94 and percent >= 90:
    grade = "A-"
elif percent < 97 and percent >= 94:
    grade = "A"
elif percent >= 97:
    grade = "A+"
elif percent < 84 and percent >= 80:
    grade = "B-"
elif percent < 87 and percent >= 84:
    grade = "B"
elif percent < 90 and percent >= 87:
    grade = "B+"
elif percent < 74 and percent >= 70:
    grade = "C-"
elif percent < 77 and percent >= 74:
    grade = "C"
elif percent < 80 and percent >= 77:
    grade = "C+"
elif percent < 64 and percent >= 60:
    grade = "D-"
elif percent < 67 and percent >= 64:
    grade = "D"
elif percent < 70 and percent >= 67:
    grade = "D+"
else:
    grade = "F"

print("You got a {:.0f}% which is a {}".format(percent,grade))

