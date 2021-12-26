# ------------------------------------------------------------
# --------------**## Exception Handling Part 1 ##**-----------

import sys

# ******------****** Example 5 ->>>> try ... except
# try:
#     age = int(input("Age: "))
# except:
#     print("please enter a valid age")


# ******------****** Example 6 ->>>> try ... except ... else
# try:
#     age = int(input("Age: "))
# except ValueError:
#     print("please enter a valid age")
# else:
#     print("No Errors Here")

# ******------****** Example 7 ->>>> try ... except ... else
# try:
#     age = int(input("Age: "))
# except ValueError as exp_error:
#     print("please enter a valid age")
#     print(exp_error)
#     print(type(exp_error))
# else:
#     print("No Errors Here")

# ******------****** Example 8 ->>>> try ... except
random_list = ["a", 0, 2]

# for entry in random_list:
#     try:
#         print("The entry is:", entry)
#         r = 1 / int(entry)
#         break
#     except:
#         print("oops!", sys.exc_info()[0], "occured.")
#         # print(sys.exc_info())
#         # print(type(sys.exc_info()))

#         print("Next entry.")
#         print()


# print()
# print("The reciprocal of", entry, "is", r)


# ******------****** Example 9 ->>>> try ... except

for entry in random_list:
    try:
        print("The entry is:", entry)
        r = 1 / int(entry)
        break
    except Exception as exp_error:
      # Exception is the same as __class__
        print("oops!", exp_error.__class__, "occured.")
        print("Next entry.")
        print()


print()
print("The reciprocal of", entry, "is", r)
