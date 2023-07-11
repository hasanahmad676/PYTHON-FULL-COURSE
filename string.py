# # a="It's is my string" # IT IS A SINGLE LINE STRING
# # print(a)


# # B='THIS IS A SINGLE LINE STRING'
# # print(B)


# # C="""
# # HERE AL THE COMMENT WILL BE MULTILINE COMMENT
# # BECAUSE WE USE THREE """"""


# # """
# # print(C)

# # positive indexing
# a="It's is my string" # IT IS A SINGLE LINE STRING
# print(a[0])


# #negative indexing
# a="It's is my string " # IT IS A SINGLE LINE STRING
# print(a[-3])

# #slicing
# print(a[0:4])
# print(a[-7:-1])
# print(a[0:4:2])# it will jump 2 psition to the right
# # print(a[-7:-1:2])# it will jump 2 position to the left

# a="hello world"
# print(a[::-1]) # it will print all the string right to left


# DELETE AND EDIT
# a="hello world"
# a[0]="H"
# print(a) # PYTHON STRING IS IMMUTABLE IT CAN NOT BE CHANGED

# a="hello world"

# del a  #it will delete whole string
# # print(a)



# Arithmetic Operations
# Relational Operations
# Logical Operations
# Loops on Strings
# Membership Operations
# a="world"

# print("hello" +" "+ "world")
# print("hello"*5)
# print('dhaka' != 'delhi')
# print('mumbai' > 'dhaka')
# print('hello' and 'world')
# print('hello' or 'world')

# for i in 'hello':
#   print(i)



# Common Functions
# 1.len
# 2.max
# 3.min
# 4.sorted

# print(len('hello world'))
# print(max('hello world'))
# print(min('hello world'))
# print(sorted('hello world'))
# print(sorted('hello world',reverse=True))


# Capitalize/Title/Upper/Lower/Swapcase

# s = 'hello world'
# print(s.capitalize())
# print(s)

# print(s.title())
# print(s.upper())
# print('Hello Wolrd'.lower())

# print('HeLlO WorLD'.swapcase())


# # Count/Find/Index
# print('my name is hasan'.count('i'))
# print('my name is hasan'.find('h'))
# print('my name is hasan'.index('a'))

# endswith/startswith
# print('my name is hasan'.startswith('i'))
# print('my name is hasan'.endswith('n'))



# format
# name = 'hasan'
# gender = 'male'

# print('Hi my name is {} and I am a {}'.format(gender,name))


# isalnum/ isalpha/ isdigit/ isidentifier

# print('hasan1234%'.isalnum())
# print('hasan1234%'.isalpha())
# print('hasan1234%'.isdigit())
# print('hasan1234%'.isidentifier())


# Split/Join
print('hi my name is hasan'.split())
print(" ".join(['hi', 'my', 'name', 'is', 'hasan']))

#Replace
print('hi my name is hasan'.replace('nitisrgewrhgh','campusx'))
#Strip
print('nitish                           '.strip())

