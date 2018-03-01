# ====== Global immutable variables ======
#
# Exercise 1: knock knock jokes
#
# a) Find and explain what is wrong in the code below
# b) Modify the functions below so as the "print(joke)" statements print the expected output.
#    - Do not move the print statement into functions
#    - Do not remove functions

# ======================================================== #
#                         VERSION 1                        #
# ======================================================== #
joke = ""
name = "Harry"
rest_answer = "up, it’s cold out here"


def make_knock_knock_joke_1():
    joke = """Knock, knock.
Who’s there?
{name}, who?
{name}{rest_answer}!""".format(name=name, rest_answer=rest_answer)


make_knock_knock_joke_1()
print("make_knock_knock_joke_1:")
print(joke)

# ======================================================== #
#                         VERSION 2                        #
# ======================================================== #
joke = """Knock, knock.
Who’s there?
{name}, who?
{name}{rest_answer}!"""
name = "Anee"
rest_answer = "one you like"


def make_knock_knock_joke_2():
    joke = joke.format(name=name, rest_answer=rest_answer)


make_knock_knock_joke_2()
print("make_knock_knock_joke_2:")
print(joke)

# ======================================================== #
#                         VERSION 3                        #
# ======================================================== #
def make_knock_knock_joke_3(joke, name, rest_answer):
    joke = joke.format(name=name, rest_answer=rest_answer)


joke = """Knock, knock.
Who’s there?
{name}, who?
{name}{rest_answer}!"""
name = "Anee"
rest_answer = "one you like"
make_knock_knock_joke_3(joke, name, rest_answer)

print("make_knock_knock_joke_3:")
print(joke)