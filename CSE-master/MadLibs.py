print("Welcome to Madlibs a game where you put in your own words into a story")
name = input("Your name: ")
name = name.upper()

sport = input("Sport: ")
sport = sport.upper()

adjective = input("Adjective: ")
adjective = adjective.upper()

title = input("Title (Mr., Ms., Prof., etc,.): ")
title = title.upper()

name2 = input("Enter another name: ")
name2 = name2.upper()

clas = input("Enter a school class: ")
clas = clas.upper()

color = input("Color: ")
color = color.upper()

color2 = input("Color 2: ")
color2 = color2.upper()

animal = input("Animal: ")
animal = animal.upper()

place = input("Place (schoolyard, quad, etc,.):  ")
place = place.upper()


print("Today {} went to their PE class where they played {} with all of the {} players".format(name,sport,adjective))
print("       NAME                                             SPORT                 ADJECTIVE")
print("{} was coached by {}{} inside of the gym".format(name,title,name2))
print(" NAME                 TITLE NAME2")
print("When {} was done with gym they had to run all the way across the campus to {}'s next class, {}".format(name,name,clas))
print("      NAME                                                                       NAME               CLASS")
print("When {} got to Mr.Grouse's {}room teacher Mr.Grouse had told {} to take a seat and listen".format(name,clas,name,name))
print("      NAME                      CLASS                                NAME")
print("However whenever Mr.Grouse had talked it seemed like the words went into one ear and out the other")
print(" ")
print("Today Mr.Grouse had a {} tie and plaid {} shirt".format(color,color2))
print("                     COLOR               COLOR2")
print("And then suddenly a wild {} went through the open door and started attacking Mr.Grouse".format(animal))
print("                        ANIMAL")
print("Everyone ran out of the building and into the {}".format(place))
print("                                               PLACE")
print("That day was the craziest school day {} ever had".format(name))
print("                                      NAME")