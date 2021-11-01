amount = 100
tax = 0.06
total = amount + amount*tax
print(total)

# Converting a float to an integer and viceversa
# amount = int(10.6)
# amount = float(10)
# Everything inside a simple or double quotes is considered a string
name = 'Julia'
print(name)
# Double quotes can be useful if a single qupte is literally part of the string: 
# store_name = "Julia's Store": yes
# store_name = 'Julia's Store': will cause an error

# Strings can be concatenated:

hello = 'Hello, '
greeting = hello + name
print(greeting)

# STDIO

my_name = input("What's your name?\n")
greeting2 = hello + my_name
print(greeting2)
