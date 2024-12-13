# So far we have only discussed whole numbers in calculations.
# However, Python supports multiple other fundamental types of data.
# We will go over these next.


# The simplest type of data we can represent is a true / false value.
# It can also be easier to think of this as an on / off value, or yes / no.
# These values are called Booleans, named after George Boole. In Python,
# this type of data is called a 'bool'.

# Here is an example of a boolean value:
myBool = True
# Here is its counterpart:
myBool = False

# We can negate (invert) a boolean using the NOT operator. This will return
# the logical inverse of the value. In other words, if the value is false it
# will return true, and if the value is true it will return false.

# You can think of this like flipping a light switch - it will always switch
# to the value opposite of what it is currently set to.

# Here is an example of the not operator:
myBool = not True

# This is equivalent to setting the variable to False:
myBool = False

# If we want to check if two or more boolean values are true, we can use the
# AND operator. This will only return true if both operands are true. It is
# easiest to think of this like the word itself - if A and B, C.

# This will set myBool equal to true:
myBool = True and True

# While this will set myBool equal to false:
myBool = True and False
# As will this,
myBool = False and True
# and this.
myBool = False and False

# You can also see if EITHER of two or more boolean values is true using the OR
# operator. Here is an example of the OR operator.

# This will set myBool equal to true.
myBool = True or False

# As will this:
myBool = True or True
# and this.
myBool = False or True

# This, however, will still set myBool equal to false.
# At least one input to the OR operator needs to be true for the result to be true.
myBool = False or False


# The next simplest type of data is a whole number. If you paid attention
# in math class, you may recall that this is referred to as an 'integer.'
# These are whole numbers - those with nothing after the decimal point.

# For example, these are integers:
x = 0
y = 6
z = -27

# While these are not:
a = 1.2
b = 3.14
c = -1.25

# a, b, and c are what are referred to as "decimals." However, there
# are some caveats to this.
# Because computers have a limited amount of memory, we cannot represent
# an infinite number of places after the decimal point.

# In the past, this issue was solved by having a fixed amount of memory
# split between the parts before and after the decimal point, like so:
w = 1234.5600

# However, this is very wasteful if we only need to represent numbers after
# the decimal point, or before the decimal point.

# To fix this, computer scientists introduced what is called a floating-point
# number. It is called floating-point because the location of the decimal point
# can vary, or "float" around the number.This solved the issue of wasting
# data, and allowed numbers with non-fixed precision, but caused some other issues.

# Those issues are somewhat beyond the scope of this course, but they become
# very relevant in the financial, scientific, and game development sectors.

# In Python, we only have access to integers and floating-point numbers. This is
# somewhat standard, as fixed-point numbers are mostly relegated to GPU programming
# since around the 90s.

# Within the language, integers are referred to as 'int's and floating-point numbers
# are referred to as 'float's.


# At this point, we can represent both whole and decimal numbers. However, each
# variable can only hold one value. While this is great for small programs, what
# happens if we need to store multiple numbers (e.g, bank account balances)? We
# could create a variable for each number, but that would require that we know the
# number of bank accounts in advance, which is incredibly unlikely.

# To solve this issue, we can instead store multiple values in one variable.
# We do this by using a construct called an array. In Python, this is referred to as
# a 'list,' like a grocery list or the list of charges on an invoice.

# Here is an example of a list.
myList = [1, 2, 3, 4, 5]

# myList contains 5 elements - the numbers 1 through 5.
# We define the contents of a list by placing them between square brackets [].

# We can access the individual elements of a list in an expression by writing the name
# of the list, then an opening square bracket '[', then an index, then a closing bracket ']'.

# Here is an example of accessing the first element of myList.
elementOne = myList[0]

# This may look like a typo at first. Why are we accessing element 0?
# This is due to the fact that computers count from zero! As a result of this, the first
# element of a list is actually located at index zero. The second is located at index 1,
# and so on.

# We can add a new element to a list by using the 'append' method.
myList.append(6)
# This will add the number 6 to the end of myList.
# If we were to print all elements of the list, it would now look like this:
# 1, 2, 3, 4, 5, 6


# At this point, we can represent integers, decimal numbers, and lists thereof. However,
# what if we want to represent text? Think about how you might do this with just lists
# and integers. Can you come up with a solution?

# In some other languages, text is represented as a list of characters (numbers representing
# a letter, number, or symbol). However, this fact is abstracted away in Python, which gives
# us a very simple type to represent text.

# This type is called a 'string,' meaning a string of characters.
# Here is an example of a string:
myString = "Hello, world!"

# We can pass this string into the print() function to display it:
print(myString)
# Which will result in "Hello, world!" appearing in the console.

# We can combine two strings by using the plus sign, just like adding numbers:
print(myString + myString)
# This may produce an unexpected result:
# Hello, world!Hello, world!

# In order to introduce a space, we must specify that explicitly.
print(myString + " " + myString)
# This will display "Hello, world! Hello, world!"

# Because strings are technically lists of characters, we can access those characters just like
# elements in a list! Those elements themselves are also strings.
myCharacter = myString[0]
# myCharacter is now equal to the string "H".

# If we multiply a string by N, it will repeat that string N times.
# For example, if we print myCharacter * 4:
print(myCharacter * 4)
# it should display "HHHH"!


