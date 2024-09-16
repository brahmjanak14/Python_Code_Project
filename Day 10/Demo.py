def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if year % 4 == 0:
        print("4")
        if year % 100 == 0:
            print("4")
            if year % 400 == 0:
                print("4")
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# Call your function with hard coded values
leap = is_leap_year(int(input("Enter the Year for check leap year or not? ")))
print(leap)