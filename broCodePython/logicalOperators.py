# logical operators (and, or, not) are used to check if two or more conditional statements are true
while(True):
    temp = int(input("What is the temperature outside? "))

    if not(temp >= 0 and temp <= 13):
        print("The temperature outside is not good!")
        print("Stay inside!")
    elif not(temp < 0 or temp > 13):
        print("It's a nice temperature outside!")
        print("You should go outside!")
