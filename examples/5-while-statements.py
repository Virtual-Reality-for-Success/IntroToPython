# A 'while' statement or 'while loop' is a block of code that repeats
# for as long as a condition is true.

# Here is a simple example:

# First, we define x, to be used as the number of times we have run
# the loop.
x = 0

# Now, we tell Python to repeat this block of code for as long as x
# is less than 5. Because we increment x by 1 every time the loop runs,
# and x starts at 0, this should run 5 times, for x = 0, 1, 2, 3, 4:
# then it should stop! This is because when x = 5, it is not less than 5!
while x < 5:
	# Remember the += operator, for adding a number to a variable?
	x += 1

# NOTE: Here we use the less-than operator '<'. You may remember this from
# math class - the alligator wants to eat the larger number, and all that.

# Here are some other useful comparison operators, for reference:
# Is X less than Y? X < Y
# Is X less than or equal to Y? X <= Y
# Is X equal to Y? x == y
# Is X greater than or equal to Y? X >= Y
# Is X greater than Y? X > Y
