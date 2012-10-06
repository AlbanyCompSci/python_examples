# Welcome to Python!
# These blocks is commented out, using the # symbol

# Print text out to screen using the print statement:
print "Hello Cougars!"  # comments can be in normal lines of code too

# You can assign strings (text, numbers, symbols, or any combination of the
# three) to variables:

variable_string = "Text1"

# Or integers/floats (integers/"decimals"):

variable_integer = 100
variable_float = 10.0

# Math operations (+, -, *, /, % [modulo; you can ignore this]):

print 100 / 10.0  # 10.0
print 100 / 10  # 10
print variable_integer / variable_float  # 10.0











# if statements:

if variable_float < variable_integer:
    # wait, what is this!?
    # Python seperates blocks of code with spacing (tabs or spaces).
    # The amount of tabs or spaces does not matter, but they must be consistant

    print "10.0 is, in fact, less than 100!"

# You can also use 'if' in combination with 'elif' and 'else':

if 1 > 2:
    pass  # don't do anything
elif "abc" == "xyz":
    pass
else:
    pass











# Lists/Dictionaries:

variable_list = ['x', 'y', 'z', 0, 1, 2]  # you can mix all data types in lists
variable_dictionary = {'dog': 'Four legged animal',  # this line break isn't
                       'fish': 'Dead meat'}          # neccessary, but it looks better

# You can loop over three primary objects:

for i in xrange(0, 10):
    print i

for item in variable_list:
    print item

for key, value in variable_dictionary.iteritems():
    print key, value  # comma inserts a space

# We skipped a little ahead there: the periods and parens are part of Python's
# function syntax

def variable_function(text):
    print text

# Any variables you create in the function are destroyed once you call the function
# i.e. variables used in functions are local variables

variable_function('Jolly good')











# Python is "batteries-included": this means it comes with a lot of COOL things/libraries
# We'll start with the basics though... these aren't really all that special:
