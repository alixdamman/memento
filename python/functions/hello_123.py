# Exercise 1: create and call a function "hello" with no argument
#
# * open the module "hello.py"
# * define a function "hello" with no arguments and make it display "Hello World !" using the print() built-in function
# * call the function
# Note: functions must be defined before being called

def hello():
    print("Hello World !")

hello()


# Exercise 2: add arguments to the function "hello"
#
# * add the arguments 'firstname' and 'surname' to the "hello" function
# * modify the function so that it displays "Hello <firstname> <surname>!"
# * call the function by passing your firstname and surname as strings
# * store your firstname and surname in variable 'fname' and 'sname' respectively
# * call the function by passing the variables 'fname' and 'sname'

def hello(firstname, surname):
    print("Hello", firstname, surname, "!")

hello("Alix", "Damman")

fname = "Alix"
sname = "Damman"
hello(fname, sname)


# Exercise 3: make function "hello" return a string
#
# * use the return statement in the "hello" function to return the string "Hello <firstname> <surname>!"
#   (instead of printing it)
# * call the function and store the returned string in a new variable 'msg'
# * display the content of 'msg' using the print() built-in function

def hello(firstname, surname):
    return "Hello {} {} !".format(firstname, surname)

msg = hello("Alix", "Damman")
print(msg)
