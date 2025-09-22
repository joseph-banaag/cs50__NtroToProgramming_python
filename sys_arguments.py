import sys

# print("hello, my name is: ", sys.argv[1], sys.argv[2])
# for this code to work, run the file and then add doks for the index 1, and banaag for the index 2.
# eg. python names.py doks banaag
# result: hello, my name is: doks banaag

# USING TRY AND EXCEPT
'''
try:
    print("hello, my name is: ", sys.argv[1], sys.argv[2])
except IndexError:
    print("please tell me your full name.")
'''

# USING IF, ELIF, ELSE
# if len(sys.argv) < 2:
#     sys.exit("Please add your firstname after the file name:")
# elif len(sys.argv) > 2:
#     sys.exit("You can only add your firstname.")
# else:
#     print("Hello, my name is: ", sys.argv[1])
# when adding two-word string inside quotes, it will be registered in index 1

# print(len(sys.argv))
# print(sys.argv[0])
# print(sys.argv[1])

for arg in sys.argv[1:]: # the slice() function added to the object sys.argv
    print(arg)
