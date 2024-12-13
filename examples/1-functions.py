# This is a function.

def function():
	print("This will be run when the function is invoked!")


# The code inside of a function will not be run until the function
# is "called."

# Functions are called by writing the name of the function, then an
# opening parenthesis, then any arguments to the function (more on
# those later), then a closing parenthesis.
function()

# Functions can also be called inside other functions.
def functionTwo():
	# This should print "This will be run when the function is invoked!"
	function()


# Functions can take input to be used. One example of this is the
# print() function, which accepts text to be shown to the user.
print("Hello, world!")

# These pieces of input are referred to as 'arguments' to the function.
# A function can have zero, one, or many arguments.

# Function arguments are defined as follows, with commas between each:

def functionWithArguments(argumentOne, argumentTwo, argumentThree):
	# The 'pass' keyword effectively means "do nothing."
	pass

# This function could then be called like so:

functionWithArguments("Argument One", 2, False)

# Note that the type of information contained in each argument is not
# strictly specified - it could be a number, text, or a true / false
# value (more on data types later!)


# Function arguments can also be optional (that is, given a default
# value). This is done by specifying their default value using an
# equals sign, much like setting a variable (more on those later).

def functionWithOptionalArgument(argumentOne = "This argument is optional."):
	print(argumentOne)

# If the user of this function does not pass a value for argumentOne,
# it will default to the value we assigned it, in this case the text
# "This argument is optional."

# Example 1:
functionWithOptionalArgument("This argument was overridden by the caller.")
# This should print "This argument was overridden by the caller."

# Example 2 (note we do not pass a value into the function):
functionWithOptionalArgument()
# This should print "This argument is optional."


# NOTE: The name of a function does not matter, as long as it is the same
# wherever it is used. Use a name that makes sense to *you*!

# This rule also applies to the names of function arguments. We can name
# the arguments whatever we want, as long as we always use the same name
# to refer to them in our code.


# One important note is that function arguments cannot be accessed outside
# the function in which they are defined.

# Think about it - the input you gave to a function is only relevant to that
# function. If we kept it around forever, the computer would run out of places
# to store that information.

# This property is referred to as the "scope" of the arguments. Every function
# has a scope, and any arguments for that function only exist within that scope.
# Later, when we discuss variables, this property will apply in a similar way.

def myFunction(myArgument):
	# This works fine, because myArgument is defined within this scope.
	print(myArgument)

# This will not work, because myArgument only exists within myFunction!
print(myArgument)
