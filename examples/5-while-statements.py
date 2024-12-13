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


# We can also exit a loop early, rather than waiting for the condition
# to be false. We can do so using the 'break' keyword.

# Let's consider the variable 'year' to be 455 AD.
# What data type is this?
year = 455

# Ordinarily, this loop will run forever!
while True:
	# This print statement will be run every year.
	print("The mighty Roman Empire will never fall!")

	# We increment the year by 1 for each iteration.
	year += 1

	# Every year, we check if it is 476 AD.
	# If the year is exactly 476, the code inside this 'if' statement
	# will be run.
	if year == 476:
		# Uh oh!
		print("Rome has fallen!")

		# Now, we end the loop.
		break

# Because of the 'break' statement, this loop has ended.
