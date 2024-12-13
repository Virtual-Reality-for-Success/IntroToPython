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


# Inside functions, we have a similar keyword, allowing us to stop
# the function early! It is called 'return':
def myFunction(stopEarly):
	# If the argument "stopEarly" is true,
	if stopEarly:
		print("Stopping early!")

		# End the function early.
		return
	
	# Otherwise, continue!
	print("... [other stuff]")


# We can also use this keyword to *return* a value back to the place
# the function was originally called. Here is an example.

def alwaysReturnsTwo():
	# This will provide the value 2 back to the caller.
	return 2

# What will X be equal to here?
# What is its data type?
x = alwaysReturnsTwo()

print(x)