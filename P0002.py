name = input("Enter your name ")
age = input("What is your age " + name + "? ")
print(name + " your age is " + age)
# print(age)
if int(age) >= 18:
    print("you are valid to Vote")

else:
    print("Please comeback in {0} years".format(18 - int(age)))
