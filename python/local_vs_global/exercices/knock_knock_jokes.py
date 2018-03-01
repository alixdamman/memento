# ====== Global immutable variables ======
#
# Exercise 1: knock knock jokes
#
# a) Find and explain what is wrong in the code below
# b) Make it print the expected knock knock jokes without moving the "print(joke)" statements


joke = ""

# ======================================================== #
def make_knock_knock_joke_1(answer):
    joke = "Knock, knock.\n Who’s there?\n"
    joke = joke + name + ", who?\n"
    joke = joke + name + answer + "!"


name = "Harry"
make_knock_knock_joke_1("up, it’s cold out here")
print("make_knock_knock_joke_1:")
print(joke)

# ======================================================== #
def make_knock_knock_joke_2(joke, name, rest_answer):
    joke = joke + name + ", who?\n"
    joke = joke + name + rest_answer + "!"


make_knock_knock_joke_2("Knock, knock.\n Who’s there?\n", "Anee", "one you like")
print("make_knock_knock_joke_2:")
print(joke)


joke = "Knock, knock.\n Who’s there?\n"
name = "Anee"
answer = "one you like"
make_knock_knock_joke_2(joke, name, answer)
print("make_knock_knock_joke_2 (bis):")
print(joke)

# ======================================================== #
joke = "Knock, knock.\n Who’s there?\n"
def make_knock_knock_joke_3(rest_answer):
    joke = joke + name + ", who?\n"
    joke = joke + name + rest_answer + "!"

name = "Justin"
make_knock_knock_joke_3("time for dinner")
print("make_knock_knock_joke_3:")
print(joke)