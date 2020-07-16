n = int(input("enter the positive no. you want to check whether it is even or odd : "))

if n%2 == 0:
    if n <= 9:
        print("single digit even number")
    else:
        print("not a single digit even number")
else:
    if n <= 9:
        print("single digit odd number")
    else:
        print("not a single digit odd number")