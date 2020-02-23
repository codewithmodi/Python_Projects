num = input("Enter a number less than 10 ")
if int(num) <= 5:
    print("please guess higher than 5")
    num = input()
    if int(num) >= 5:
        print("Well done")
    else:
        print("Your are still short of no")
else:
    print("Your chosen number is " + num)
    print("Well done")

