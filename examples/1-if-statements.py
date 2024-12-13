# 'if' statements are one of the most fundamental constructs in computer
# programming. They allow your program to make decisions, taking a
# branching path through your code rather than one that is constant.

# Here is a basic 'if' statement.
# The double equals sign '==' compares two values. It results in a 'true'
# value if the values are equal, and a 'false' value if they are not.
if 1 == 0:
	# Since 1 does not equal 0, this 'print' statement should never run.
	print("Something doesn't seem right here.")


# One counterpart to the 'if' statement is the 'else' statement. If used,
# it must immediately follow the contents of either an 'if' statement or
# an 'elif' statement (more on that in a moment). It will only be run if
# all previous sections of the 'if' statement do not run.

# Here is an example of an 'if..else' statement.
if 1 == 0:
	# Since 1 does not equal 0, this 'print' statement should never run.
	print("This still seems off.")
else:
	# The 'else' statement immediately follows the contents of the 'if'
	# statement. Since the previous 'if' statement always gets skipped,
	# this 'else' statement should always run.
	print("This seems much better!")


# The last component of an 'if' statement is the 'elif' statement. In
# other languages, this is sometimes written as 'else if' rather than
# one word. They mean the same thing - an 'else' statement which depends
# on yet another condition. This is clearer with an example.

# Here is an example of an 'if..elif' statement. There is no 'else'
# statement, though one could be included.
if 1 == 0:
	# This statement should never run.
	print("This is starting to get weird.")
elif 0 == 0:
	# Because the previous statement never runs, Python will check the
	# expression that 'elif' depends on (0 == 0). If and only if that
	# evaluates to true, this block will be run. If it were not true,
	# this block would be skipped would 
	print("There we go!")

# To make sure you get the point, here is another example.
if 0 == 0:
	# This block of code should always run.
	print("That checks out!")
elif 1 == 1:
	# Despite the fact this condition always turns out to be true,
	# it will never be checked! This is because the 'if' statement
	# is always run, which then skips all successive 'elif' statements.
	print("Despite the fact this is true, it will never run.")
else:
	# Because the 'if' statement always runs, this statement will be skipped
	# along with the 'elif' statement.
	print("This will never run either!")

# This is a slightly different example. Can you spot what will happen?
if 1 == 0:
	# This block of code should never run.
	print("This is just getting weird.")
elif 1 == 1:
	# Because 1 is equal to 1 and the 'if' statement is always false,
	# this block of code should run every time.
	print("This is behaving correctly!")
else:
	# Despite the fact the 'if' statement never runs, this block shouldn't
	# run either. This is because the 'elif' statement will skip all successive
	# 'elif' and 'else' statements if it runs, whici it does every time.
	print("Something seems off.")


# 'elif' statments can also be chained to perform multiple checks that stop when
# one ends up being true.

# Here is an example:
if False:
	print("This code will never run.")
elif False:
	print("This code will not run either.")
elif True:
	print("This code will always run.")
	# This 'elif' statement evaluating to 'true' will also skip all those after it:
elif True:
	# Even though this 'elif' statement would ordinarily always run if given the chance,
	# it will never run because it is skipped by the previous 'elif' statement.
	print("Too slow :(")
else:
	# Because one of the 'if' or 'elif' statements before this 'else' runs at some point,
	# this 'else' statement will never be executed.
	print("This code will never run.")


# One last helpful property of 'if' statements is that because they are statements like any
# other, they can be placed within other 'if,' 'elif,' or 'else' statements.

# Here is an example of a nested 'if' statement.
if 1 == 1:
	print("This should always run.")

	if 0 == 0:
		print("This should always run as well!")

# Note that if the outer 'if' statement evaluates to false, all code inside it will not be run:
if False:
	print("This will never run.")

	if True:
		# Because this is inside a block of code that will never be run, even though the 'if'
		# statement is always true, it will not be checked and therefore cannot be run.
		print("Even though this would run given the chance, it can't!")
