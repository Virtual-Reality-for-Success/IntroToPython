# A variable is a way of storing a value that can *vary,* hence
# the name. You can think of it like a box that you put the value
# in.

# The name of the variable doesn't matter - as long as it's the
# same every time you use it! You can think of the variable's name
# like what you write on the outside of the box. It doesn't need to
# be anything in particular, as long as it makes sense to you. Even
# if it doesn't, it won't really affect what's on the inside of the
# box.

# Variables in python are defined without using any sort of keyword.
# In other languages you will often see words like "var" being used.
# Fun fact - variables in math are often defined using "let," which
# is what the Rust programming language uses!

# Here's a simple example:
x = 1

# This will print "1"
print(x)

# This will print "2"
print(x + x)
# as will this (the asterisk means "multiplied by," like the multiplication dot '⋅').
print(x * 2)


# The value inside a variable can be changed the same way it was
# originally defined:
x = 2

# This will print "2" now.
print(x)


# You can also use the value of a variable in an expression:
if x == 2:
	# This will only run if x is equal to 2, which it is.
	print("x is equal to 2")


# You can even use a variable in the expression used to reassign it!
x = x * 2

# Because x was equal to 2, it should now be equal to 2 * 2 = 4!
print(x)


# Some reassignment operations have short forms that can be used instead.
# For example, assuming we have a variable:
y = 1

# Here is a possible operation we can perform on it, incrementing it by 1.
y = y + 1

# Here is a shorter form we can use, built into the language:
y += 1
# The statement y += XYZ is equivalent to the statement y = y + XYZ.
