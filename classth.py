name : str = "muhammad"
print(name)
print(id(name))
print(type(name))
print(dir(name))
#for index
print(name[1])
#methods:
#capitalize(capitalize only first character)
print(name.capitalize())
#format(insert the value inside the place holder)

name = "John"
age = 25

# Using positional arguments
sentence = "My name is {} and I am {} years old.".format(name, age)
print(sentence)
# Using positional arguments with indexes
sentence = "My name is {0} and I am {1} years old.".format(name, age)
print(sentence)
# Using keyword arguments
sentence = "My name is {n} and I am {a} years old.".format(n=name, a=age)
print(sentence)

#casefold(it is little difrent from lower as it adds some more transformation)
txt = "Hello, And Welcome To My World"

print(txt.casefold())

#center
fruit = "banana"

x = fruit.center(20)

print(x)
#--------------------------
classname = "Python"
classname2 = classname.center(10)

print(classname2)

#count
quote = "I love apples, apple are my favorite fruit"

a = quote.count("apple")

print(a)
#------------------
program = "Python is powerful. Python is easy to learn. Python is fun."

b = program.count("Python")
print("Number of occurrences of 'Python':", b)

#encode
statement = "My name is Ståle"

x = statement.encode()

print(x)

#endswith
text = "Hello, welcome to my world."

y = text.endswith(".")

print(y)
#---------------
text1 = "python is programming language"
z = text1.endswith("e")
print(z)

text1 = "python is programming language"
z = text1.endswith("g")
print(z)

#expand tab
# txt ="h\te\tl\tl\to"

# # x =  txt.expandtabs(2)

# print(txt)

txt ="h\te\tl\tl\to"

x =  txt.expandtabs(2)

print(txt)
#--------------------------------------


abc = "h\te\tl\tl\to"

# Replace tabs with 4 spaces
c = abc.expandtabs(4)

print(abc)  # Original string
print(c)    # String after expanding tabs

#find
find = "Hello, welcome to my world."

x = find.find("to")

print(x)

#isalnum(all characters in text is alphanumeric)
isl = "Company12"

x = isl.isalnum()

print(x)
#isalpha(all characters in text are letters)
let = "CompanyX"

x = let.isalpha()

#isascii((American Standard Code for Information Interchange)
asc = "Company123"

x = asc.isascii()

print(x)
#isdecimal(0-9)
dec = "1234"

x = dec.isdecimal()

print(x)
#isdigit
txt = "50800"

x = txt.isdigit()

print(x)

#isidentifier
idt = "Demo"

x = idt.isidentifier()

print(x)

#islower
txt = "hello world!"

x = txt.islower()

print(x)

#is numeric
txt = "565543"

x = txt.isnumeric()

print(x)

#isprintable
txt = "Hello! Are you 1?"

x = txt.isprintable()

print(x)

#isspace
txt = "   "

x = txt.isspace()

print(x)

#istitle(each letter starts with upper case result return in true or false)
txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)

#title
txt = "Welcome to my world"

x = txt.title()

print(x)
#isupper(return true or false)
txt = "THIS IS NOW!"

x = txt.isupper()

print(x)

#join
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

#ljust(return left justified version)
txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")

#------------------------

txt = "banana"

x = txt.ljust(20, "O")

print(x)

#rjust(return right justified version)
txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")
#upper(all characters)
txt = "Hello my friends"

x = txt.upper()

print(x)

#lower
txt = "Hello my FRIENDS"

x = txt.lower()

print(x)

#strip
txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")

#lstrip  (remove spaces to left)
txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")

#maketrans(rule maker)
#translate(rule applier)
txt = "Hello Sam!"

mytable = str.maketrans("S", "P")

print(txt.translate(mytable))

#partition(return tuple)
txt = "I could eat bananas all day"

x = txt.partition("bananas")
#rsplit(convert string into list using square bracket, comma,followed by space)
txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)



print(x)

#replace
txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

#rfind(find the last occurance of letter e)
txt = "Hello, welcome to my world."

x = txt.rfind("e")

print(x)

#rindex
txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)

#splitlines
txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)

#startswith
txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)

#swapcase
txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)

#zfill
txt = "50"

x = txt.zfill(20)

print(x)





