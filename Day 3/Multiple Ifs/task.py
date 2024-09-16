print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")

    if age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")

    take_photo_Ans = input("Can you ride on click the photo (y/n): ")
    if take_photo_Ans == 'y':
        bill+=3
        print("you have to pay: $"+str(bill))
    else:
        print("You have to pay only: $"+str(bill))
