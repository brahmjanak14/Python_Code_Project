from gc import get_referents


def mynew_fun():
    print("Hello World")

mynew_fun()


def get_user_name():
    name = input("What is your name? ")
    print("Hello, " + name)
    #Inside the function

#outside function
get_user_name() # calling the function