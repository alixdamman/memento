# ====== Global non-array variables - Exercise 1 ======
#
# Exercise 1: knock knock jokes
#
#   a) This Python script is supposed to print 3 different "knock knock" jokes
#      but there is something wrong in the code.
#   b) Find and explain what is wrong in the code.
#   b) Modify the functions so as the "print(joke)" statements print
#      the "knock knock" jokes as expected.
#      - Do not move the print statement into functions!
#      - Do not remove functions!


# ======================================================== #
#           ORIGINAL CODE WITH EXPLANATIONS                #
# ======================================================== #


# ======================================================== #
#                         VERSION 1                        #
# ======================================================== #
joke = ""
name = "Harry"
rest_answer = "up, it’s cold out here"

# EXPLANATION: the use of operator '=' creates a new local variable 'joke'.
# Inside the function, the global variable 'joke' is shadowed by the local variable 'joke'.
# The global variable 'joke' remains unchanged.
def make_knock_knock_joke_1():
    joke = """Knock, knock.
Who’s there?
{name}, who?
{name}{rest_answer}!""".format(name=name, rest_answer=rest_answer)


# make_knock_knock_joke_1()
# print("make_knock_knock_joke_1:")
# print(joke)

# ======================================================== #
#                         VERSION 2                        #
# ======================================================== #
joke = """Knock, knock.
Who’s there?
{name}, who?
{name}{rest_answer}!"""
name = "Anee"
rest_answer = "one you like"


# EXPLANATION: the use of operator '=' creates a new local variable 'joke'.
# Inside the function, the global variable 'joke' is shadowed by the local
# variable 'joke' and is NO longer accessible.
# Calling the function below throws an error because after operator '='
# we try to access a local variable that has not been assigned yet.
def make_knock_knock_joke_2():
    joke = joke.format(name=name, rest_answer=rest_answer)


# make_knock_knock_joke_2()
# print("make_knock_knock_joke_2:")
# print(joke)

# ======================================================== #
#                         VERSION 3                        #
# ======================================================== #
# EXPLANATION: input arguments are local variables.
# The return statement must be used at the end this function to
# return the content of the local 'joke' variable
def make_knock_knock_joke_3(joke, name, rest_answer):
    joke = joke.format(name=name, rest_answer=rest_answer)


joke = """Knock, knock.
Who’s there?
{name}, who?
{name}{rest_answer}!"""
name = "Anee"
rest_answer = "one you like"
make_knock_knock_joke_3(joke, name, rest_answer)

# print("make_knock_knock_joke_3:")
# print(joke)


# ======================================================== #
#                         SOLUTION                         #
# ======================================================== #
# Use only local variables:
# 1) declare 'name' and 'rest_answer' as input parameters
# 2) use the return statement at the end to return the local variable 'joke'
def make_knock_knock_joke(name, rest_answer):
    joke = """Knock, knock.
Who’s there?
{name}, who?
{name} {rest_answer}!""".format(name=name, rest_answer=rest_answer)
    return joke


joke = make_knock_knock_joke("Harry", "up, it’s cold out here")
print(joke)

print()

joke = make_knock_knock_joke("Anee", "one you like")
print(joke)