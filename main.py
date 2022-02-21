#Modify this code so it does not use magic numbers and instead uses a constant

ounces = int(input("How many ounces does the recipe need? "))
# There are 8 ounces in a cup, so calculate the exact number of cups
# Use integer division so we don't have a remainder
cups = ounces // 8
# Whatever is not an even multiple of 8 is the remaining number of ounces
ounces = ounces % 8

print("That is", cups, "cups, and", ounces, "ounces")
